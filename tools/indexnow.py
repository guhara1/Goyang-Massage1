#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — 빙·네이버·얀덱스 등 IndexNow 참여 검색엔진.

글을 올리거나 사이트를 갱신한 뒤 한 번 실행하면 sitemap.xml 의 모든 URL을
IndexNow 엔드포인트로 통보해 즉시 색인 요청을 보냅니다.

사용법:
    python3 tools/indexnow.py                 # sitemap.xml 의 전체 URL 통보
    python3 tools/indexnow.py URL [URL ...]   # 지정한 URL만 통보(글 1건 등)
    python3 tools/indexnow.py --dry-run       # 전송 없이 대상만 출력

전제:
    - content/site.py 의 BASE_URL 이 실제 배포 도메인이어야 합니다.
    - https://<도메인>/<INDEXNOW_KEY>.txt 가 접근 가능해야 합니다(빌드 시 자동 생성).
"""
import json
import os
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

# api.indexnow.org 는 참여 검색엔진(빙·네이버·얀덱스·Seznam)에 함께 전달합니다.
ENDPOINT = "https://api.indexnow.org/indexnow"


def sitemap_urls(path):
    tree = ET.parse(path)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [loc.text.strip() for loc in tree.findall(".//sm:loc", ns)]


def submit(urls):
    base = BASE_URL.rstrip("/")
    host = base.split("://", 1)[-1].split("/", 1)[0]
    payload = {
        "host": host,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{base}/{INDEXNOW_KEY}.txt",
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.status, resp.read().decode("utf-8", "replace")


def main():
    args = [a for a in sys.argv[1:] if a != "--dry-run"]
    dry = "--dry-run" in sys.argv

    if args:
        urls = args
    else:
        sm = os.path.join(ROOT, "sitemap.xml")
        if not os.path.exists(sm):
            sys.exit("sitemap.xml 이 없습니다. 먼저 python3 build.py 를 실행하세요.")
        urls = sitemap_urls(sm)

    if "example.com" in BASE_URL:
        sys.exit("content/site.py 의 BASE_URL 이 예시 도메인입니다. 실제 도메인으로 바꾸세요.")

    print(f"대상 {len(urls)}개 URL · key={INDEXNOW_KEY}")
    for u in urls:
        print("  ", u)
    if dry:
        print("[dry-run] 전송하지 않았습니다.")
        return

    try:
        status, body = submit(urls)
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {e.read().decode('utf-8', 'replace')}")
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"네트워크 오류: {e}")
        sys.exit(1)

    # 200/202 = 정상 접수
    print(f"응답: HTTP {status} {body or '(본문 없음)'}")
    if status in (200, 202):
        print("✓ IndexNow 통보 완료 (빙·네이버·얀덱스에 전달됨)")
    else:
        print("⚠ 응답 코드를 확인하세요.")


if __name__ == "__main__":
    main()
