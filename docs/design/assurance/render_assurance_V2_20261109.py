#!/usr/bin/env python3
"""Second edition, derived from render_assurance_20261109.py.

D2 places both vertical lanes inside a horizontal grid. Its cross-grid edges
are straight, so these edges are routed in the empty handoff/top gutters.
This changes neither topology, labels, colors nor shapes. All downloaded tools,
fonts, intermediate SVG and fontconfig caches remain in the ignored .cache/.
"""
from __future__ import annotations

import base64
import os
from pathlib import Path
import re
import subprocess
from lxml import etree as ET

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
RESOURCES = ROOT / '.cache/assurance-diagram'
CACHE = RESOURCES / 'v2'
D2 = RESOURCES / 'tools/d2-v0.9.0/bin/d2'
FONTS = RESOURCES / 'fonts'
NAME = 'ASSURANCE_PROCESS_V2_20261109'
NS = '{http://www.w3.org/2000/svg}'


def main() -> None:
    fonts = []
    for kind, weight in [('regular', 'Regular'), ('bold', 'Bold'),
                         ('semibold', 'Bold'), ('italic', 'Regular')]:
        fonts += [f'--font-{kind}', str(FONTS / f'NotoSansSC-{weight}.ttf')]
    CACHE.mkdir(parents=True, exist_ok=True)
    canonical = (HERE / f'{NAME}.d2').read_text()
    # Feedback edges are drawn below after the ELK forward-flow layout, so
    # cycle breaking cannot move X1 below the roles it owns. The canonical
    # D2 file retains every prescribed edge and remains the topology source.
    lines = []
    for line in canonical.splitlines():
        feedback = (' -> ' in line and
                    any('class: '+c in line for c in ['back', 'proposal', 'evidence', 'revision']) and
                    not line.strip().startswith('a -> b:'))
        if not feedback:
            lines.append(line)
    forward = CACHE / 'forward-layout.d2'
    forward.write_text('\n'.join(lines)+'\n')
    raw = CACHE / 'layout.svg' 
    subprocess.run([str(D2), '--layout=elk', '--pad', '40', '--scale', '1',
                    '--elk-nodeNodeBetweenLayers', '60',
                    '--elk-edgeNodeBetweenLayers', '16', *fonts,
                    str(forward), str(raw)], check=True)
    tree = ET.parse(str(raw))
    root = tree.getroot()
    inner = root.find(NS + 'svg')
    assert inner is not None

    def shape(key):
        code = base64.b64encode(key.encode()).decode()
        return next(x for x in inner.xpath('.//*[@class]')
                    if code in x.get('class', '').split())

    def rect(key):
        item = shape(key).find('.//' + NS + 'rect')
        assert item is not None, key
        return tuple(float(item.get(k)) for k in ('x', 'y', 'width', 'height'))

    def edge(source, target, index=0):
        return shape(f'({source} -&gt; {target})[{index}]')

    def label(group, x, y):
        text = group.find(NS + 'text')
        assert text is not None
        text.set('x', str(x))
        text.set('y', str(y))
        for span in text.findall(NS + 'tspan'):
            span.set('x', str(x))

    def route(group, points):
        path = group.find(NS + 'path')
        assert path is not None
        path.set('d', 'M ' + ' L '.join(f'{x:g} {y:g}' for x, y in points))
        path.attrib.pop('mask', None)

    def feedback(source, target, words, kind, width=None, optional=False):
        assert words.replace('\n', '\\n') in canonical, words
        line = next(x for x in canonical.splitlines() if x.startswith('  '+kind+':'))
        color = re.search(r'stroke: "(#[A-Fa-f0-9]+)"', line)[1]
        text_color = re.search(r'font-color: "(#[A-Fa-f0-9]+)"', line)[1]
        weight = width or float(re.search(r'stroke-width: ([0-9.]+)', line)[1])
        group = ET.SubElement(inner, NS+'g', attrib={'data-source': source, 'data-target': target,
                                                    'data-kind': kind, 'data-optional': str(optional).lower()})
        marker_id = 'v2-feedback-'+str(len(inner))
        marker = ET.SubElement(group, NS+'marker', id=marker_id, markerWidth='18', markerHeight='18',
                               refX='13', refY='9', viewBox='0 0 18 18', orient='auto', markerUnits='userSpaceOnUse')
        ET.SubElement(marker, NS+'path', d='M 1 1 L 17 9 L 1 17 Z', fill=color)
        dash = 'stroke-dasharray:15,14;' if optional else ''
        ET.SubElement(group, NS+'path', d='M 0 0 L 1 1', stroke=color, fill='none',
                      attrib={'class':'connection', 'style':f'stroke-width:{weight};'+dash,
                              'marker-end':f'url(#{marker_id})'})
        text = ET.SubElement(group, NS+'text', x='0', y='0', fill=text_color,
                             attrib={'class':'text-bold' if kind=='back' else 'text',
                                     'style':'text-anchor:middle;font-size:25px'})
        for i, word in enumerate(words.splitlines()):
            ET.SubElement(text, NS+'tspan', x='0', dy='0' if i==0 else '30').text=word
        return group

    def badge(cx, cy):
        group = ET.SubElement(inner, NS+'g', attrib={'data-notice':'动手前、完成后都告知用户'})
        ET.SubElement(group, NS+'rect', x=str(cx-200), y=str(cy-24), width='400', height='48',
                      fill='#FDE68A', stroke='#92400E', attrib={'style':'stroke-width:2'})
        ET.SubElement(group, NS+'text', x=str(cx), y=str(cy+8), fill='#111827',
                      attrib={'class':'text', 'style':'text-anchor:middle;font-size:24px'}).text='动手前、完成后都告知用户'

    def diamond(key):
        text = shape(key).find(NS+'text')
        return float(text.get('x')), float(text.get('y'))-7, 225.0, 125.0

    lx, ly, lw, lh = rect('design')
    hx, hy, hw, hh = rect('handoff')
    rx, ry, rw, rh = rect('delivery')
    dx, dy, dw, dh = rect('design.owner')
    ex, ey, ew, eh = rect('delivery.owner')
    ax, ay, aw, ah = rect('design.approve')
    mx, my, mw, mh = rect('design.merge')
    ix, iy, iw, ih = rect('delivery.implement')
    vx, vyy, vww, vhh = rect('delivery.validator')
    doc = shape('handoff.contract')
    center_x = float(doc.find(NS+'text').get('x'))
    first = doc.find('.//'+NS+'path')
    old_doc_y = float(re.match(r'M\s+[-\d.]+\s+([-\d.]+)', first.get('d'))[1])
    doc_h, doc_w = 360.0, 360.0
    doc_y = (lh-doc_h)/2
    doc.set('transform', f'translate(0 {doc_y-old_doc_y:g})')
    left, right = center_x-doc_w/2, center_x+doc_w/2
    mid_y = doc_y+doc_h/2
    gutter_left, gutter_right = lx+lw+43, rx-43
    route(edge('design.approve', 'handoff.contract'), [
        (ax+aw+3, ay+ah/2), (gutter_left, ay+ah/2), (gutter_left, mid_y), (left-7, mid_y)])
    route(edge('handoff.contract', 'delivery.owner'), [
        (right+3, mid_y), (gutter_right, mid_y), (gutter_right, ey+eh/2), (ex-7, ey+eh/2)])

    red = feedback('delivery.owner','design.owner',
                   '退回请求\n合同矛盾或缺决定\n新事实推翻设计\n验收器做不到或判据不对\n需要用户才能定的事','back',8)
    outer_right, outer_left = rx+rw+75, lx-55
    route(red, [(ex+ew+3,ey+eh*.2), (outer_right,ey+eh*.2), (outer_right,-90),
                (outer_left,-90), (outer_left,dy+dh*.3), (dx-7,dy+dh*.3)])
    label(red, (dx+ex+ew)/2, -275)
    orange=feedback('delivery.owner','design.owner','验收器提案：D1 决定是否采纳','proposal')
    route(orange, [(ex-3,ey+eh*.75),(rx-15,ey+eh*.75),(rx-15,-20),
                   (lx+15,-20),(lx+15,dy+dh*.65),(dx-7,dy+dh*.65)])
    label(orange,(dx+ex+ew)/2,-37)
    proposal=feedback('delivery.validator','delivery.owner','验收器提案','proposal')
    ymid=(ey+eh+vyy)/2
    route(proposal,[(vx+vww*.7,vyy-3),(vx+vww*.7,ymid),
                    (ex+ew*.25,ymid),(ex+ew*.25,ey+eh+7)])
    label(proposal,(vx+vww*.7+ex+ew*.25)/2,ymid-14)

    purple=feedback('design.owner','handoff.contract','小修订：新版本，只重跑结构检查','revision')
    small_y=dy+dh*.85
    route(purple,[(dx+dw+3,small_y),(lx+lw+17,small_y),(lx+lw+17,doc_y+55),(left-7,doc_y+55)])
    small_x=(dx+dw+lx+lw+17)/2
    label(purple,small_x,small_y-50)
    badge(small_x,small_y)
    major=feedback('design.owner','design.merge','大改：重新过关卡','back')
    major_y=my+mh*.65
    route(major,[(dx-3,dy+dh*.85),(lx+45,dy+dh*.85),(lx+45,major_y),(mx-7,major_y)])
    major_x=(lx+45+mx)/2
    label(major,major_x,major_y-50)
    badge(major_x,major_y)
    pxc,pyc,pw,ph=diamond('design.pass')
    back=feedback('design.pass','design.merge','否：补缺口','back')
    route(back,[(pxc-pw/2-3,pyc),(lx-15,pyc),(lx-15,my+mh*.3),(mx-7,my+mh*.3)])
    label(back,lx-15,pyc-30)
    pxc,pyc,pw,ph=diamond('delivery.pass')
    repair=feedback('delivery.pass','delivery.implement','否，属实现问题：返修','back')
    route(repair,[(pxc+pw/2+3,pyc),(rx+rw+35,pyc),
                  (rx+rw+35,iy+ih*.7),(ix+iw+7,iy+ih*.7)])
    label(repair,(pxc+pw/2+rx+rw+35)/2,pyc-24)
    for key,optional,offset,entry in [('professional',True,18,.5),('judge',False,45,.8)]:
        qx,qy,qw,qh=rect('delivery.'+key)
        evidence=feedback('delivery.'+key,'delivery.owner','只交证据','evidence',2,optional)
        line_x=rx+rw-offset
        evidence_y=qy+qh*.65
        route(evidence,[(qx+qw+3,evidence_y),(line_x,evidence_y),
                        (line_x,ey+eh*entry),(ex+ew+7,ey+eh*entry)])
        label(evidence,(qx+qw+line_x)/2,evidence_y-18)

    # A single horizontal legend; preserve solid/dashed as required/optional.
    for name in ['required','optional','normal','back','proposal','revision','evidence']:
        sample=shape(f'legend.{name}.(a -&gt; b)[0]')
        path=sample.find(NS+'path')
        pts=[float(x) for x in re.findall(r'-?\d+(?:\.\d+)?',path.get('d'))]
        center=(pts[0]+pts[-2])/2
        route(sample,[(center-65,pts[1]),(center+65,pts[1])])

    # Retain D2's embedded subset fonts for SVG readers; fontconfig provides
    # the same Noto Sans SC font to librsvg when writing the PNG.
    style = ET.SubElement(inner, NS + 'style')
    css = '\n'.join(inner.xpath('./*[local-name()="style"]/text()')[:-1])
    families = re.findall(r'font-family:\s*[\'"]?([^;\n\'"}]+)', css)
    families = [x.strip() for x in families if 'font-' in x]
    regular = next((x for x in families if 'font-regular' in x), 'Noto Sans SC')
    bold = next((x for x in families if 'font-bold' in x), 'Noto Sans SC')
    style.text = (
        f'.text, .text-italic {{font-family: "{regular}", "Noto Sans SC", sans-serif; font-style: normal;}}\n'
        f'.text-bold {{font-family: "{bold}", "Noto Sans SC", sans-serif; font-weight: 700;}}')

    old_w, old_h = float(root.get('width')), float(root.get('height'))
    top_pad = 325.0
    # The outer red return sits beyond the right lane: reserve its full bend
    # and stroke, then expand height as needed instead of clipping horizontally.
    view_w = max((old_h+top_pad)*1.6, old_w+410)
    view_h = view_w/1.6
    view_x = (old_w-view_w)/2
    inner.tag = NS+'g'
    for key in list(inner.attrib):
        if key != 'class':
            del inner.attrib[key]
    inner.set('transform', 'translate(40 40)')
    root.set('width', '2400')
    root.set('height', '1500')
    root.set('viewBox', f'{view_x:g} {-top_pad:g} {view_w:g} {view_h:g}')
    root.set('role', 'img')
    title = ET.Element(NS+'title')
    title.text = 'Design Assurance 与 Delivery Assurance 合并流程草案 第二版'
    root.insert(0, title)
    background = ET.Element(NS+'rect', x=str(view_x), y=str(-top_pad),
                            width=str(view_w), height=str(view_h), fill='#FFFFFF')
    root.insert(1, background)
    svg = HERE/f'{NAME}.svg'
    tree.write(str(svg), encoding='utf-8', xml_declaration=True)

    config = CACHE/'fonts.conf'
    config.write_text(f'''<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig><dir>{FONTS}</dir><cachedir>{CACHE/'font-cache'}</cachedir>
<alias><family>sans-serif</family><prefer><family>Noto Sans SC</family></prefer></alias>
</fontconfig>''')
    env = os.environ.copy()
    env['FONTCONFIG_FILE'] = str(config)
    env['XDG_CACHE_HOME'] = str(CACHE/'xdg-cache')
    subprocess.run(['rsvg-convert', '-w', '4800', '-h', '3000',
                    '-o', str(HERE/f'{NAME}.png'), str(svg)], env=env, check=True)
    print('V2 SVG 2400×1500; PNG 4800×3000; Noto Sans SC')


if __name__ == '__main__':
    main()
