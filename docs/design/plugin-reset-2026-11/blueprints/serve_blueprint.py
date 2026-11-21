#!/usr/bin/env python3
"""Loopback-only blueprint server; Python standard library only."""
import argparse
import json
import os
import re
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

BASE = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("plugin")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", args.plugin):
        parser.error("invalid plugin")
    directory = BASE / args.plugin
    data = json.loads((directory / "blueprint.yaml").read_text(encoding="utf-8"))
    ids = {"todos": {t["id"] for t in data["todos"]},
           "regressions": {r["id"] for r in data["regressions"]}}
    decisions_path = directory / "decisions.yaml"
    lock = threading.Lock()

    def read_decisions():
        result = json.loads(decisions_path.read_text(encoding="utf-8"))
        if set(result) != set(ids):
            raise ValueError("invalid decision groups")
        for group, keys in ids.items():
            if set(result[group]) != keys or any(value not in (None, "0.1", "0.2", "搁置") for value in result[group].values()):
                raise ValueError("invalid decisions")
        return result

    read_decisions()

    class Handler(BaseHTTPRequestHandler):
        def respond(self, status, body, content_type="application/json; charset=utf-8"):
            if isinstance(body, (dict, list)):
                body = (json.dumps(body, ensure_ascii=False) + "\n").encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            self.wfile.write(body)

        def same_origin(self):
            allowed = {f"127.0.0.1:{args.port}", f"localhost:{args.port}"}
            origin = self.headers.get("Origin")
            return self.headers.get("Host") in allowed and (origin is None or origin in {f"http://{host}" for host in allowed})

        def do_GET(self):
            if not self.same_origin():
                return self.respond(403, {"error": "origin"})
            path = urlsplit(self.path).path
            if path == "/favicon.ico":
                return self.respond(204, b"", "image/x-icon")
            if path == "/api/decisions":
                with lock:
                    return self.respond(200, {"plugin": args.plugin, "decisions": read_decisions()})
            files = {"/": ("index.html", "text/html; charset=utf-8"),
                     "/index.html": ("index.html", "text/html; charset=utf-8"),
                     "/" + data.get("font", "NotoSansSC.ttf"): (data.get("font", "NotoSansSC.ttf"), "font/ttf")}
            if path not in files:
                return self.respond(404, {"error": "not found"})
            name, content_type = files[path]
            target = (directory / name).resolve()
            if not target.is_relative_to(directory.resolve()) or not target.is_file():
                return self.respond(404, {"error": "not found"})
            self.respond(200, target.read_bytes(), content_type)

        def do_POST(self):
            if not self.same_origin():
                return self.respond(403, {"error": "origin"})
            if urlsplit(self.path).path != "/api/decisions":
                return self.respond(404, {"error": "not found"})
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if not 0 < length <= 4096 or self.headers.get_content_type() != "application/json":
                    raise ValueError("invalid request")
                change = json.loads(self.rfile.read(length))
                if set(change) != {"group", "id", "value"}:
                    raise ValueError("invalid fields")
                group, id_, value = change["group"], change["id"], change["value"]
                if group not in ids or id_ not in ids[group] or value not in (None, "0.1", "0.2", "搁置"):
                    raise ValueError("invalid choice")
            except (ValueError, TypeError):
                return self.respond(400, {"error": "invalid choice"})
            with lock:
                decisions = read_decisions()
                decisions[group][id_] = value
                temporary = decisions_path.with_suffix(".yaml.new")
                with temporary.open("w", encoding="utf-8") as stream:
                    stream.write(json.dumps(decisions, ensure_ascii=False, indent=2) + "\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                os.replace(temporary, decisions_path)
            self.respond(200, {"saved": True})

    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    print(f"http://127.0.0.1:{args.port}/", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
