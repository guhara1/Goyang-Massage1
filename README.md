# 바로 GO — 고양 출장마사지·홈타이 안내 사이트

경기도 고양시 전지역(덕양구·일산동구·일산서구) 방문 관리(출장마사지·홈타이) 안내용 정적 사이트입니다.
상호: **바로 GO** · 전화예약: **0508-202-4719**

## 구조

- 정적 HTML 사이트 — 어느 호스팅(GitHub Pages, Netlify, 일반 웹서버)에서든 그대로 서빙 가능
- `build.py` + `content/` 패키지에서 페이지를 생성하는 빌드 방식
- 생성물(각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`)도 저장소에 포함

```
build.py            # 빌드 스크립트 (레이아웃·글자수 검사·sitemap 생성)
content/
  site.py           # 상호·전화·BASE_URL·메뉴·지역 데이터(단일 소스)
  main.py           # 고양 메인 페이지 (+ Organization/WebPage/FAQPage JSON-LD)
  districts.py      # 구별 안내 + 지역별(대표동) 허브 + 3개 구 페이지
  dongs.py          # 대표동 30개 (덕양 15·일산동 8·일산서 7)
  stations.py       # 역세권: 허브 + 16개 역
  areas.py          # 생활권(거점): 허브 + 14개 생활권
  info.py           # 예약 안내·이용 전 확인사항·홈타이 가이드·고객센터·약관
  about.py          # 사이트 소개 (E-E-A-T)
assets/             # CSS(프리미엄 토큰), 모바일 내비 JS
```

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수 리포트가 출력됩니다.

## SEO 운영 원칙 (빌드에 강제됨)

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리되고 sitemap에서 제외
- 번호 행정동(화정1·2동, 행신1~4동 등)은 **대표동으로 통합** — 개별 페이지 없음
- 역은 역 1개당 페이지 1개 — **환승역도 URL 하나**, 예정역·미개통역 색인 페이지 없음
- 메뉴·URL에 "출장마사지" 키워드 반복 없음 — Title·H1·첫 문단에서만 자연 사용
- 모든 페이지 본문은 페이지별 고유 작성 (지역명만 바꾼 복붙 없음)
- 메타 디스크립션은 80자 이내

## 배포 전 해야 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. `content/site.py`의 `TELEGRAM_SITE`/`TELEGRAM_BIZ`(제작·제휴 문의 텔레그램) 확인
3. `python3 build.py` 재실행 (canonical·sitemap·robots.txt에 반영됨)
4. Google Search Console에 `sitemap.xml` 제출

## 색인/인덱싱 (네이버·구글·빙)

빌드 시 자동 생성되는 파일:

- `sitemap.xml` — 색인 대상 URL + `lastmod`
- `rss.xml` — RSS 2.0 피드(네이버·피드 기반 발견용)
- `robots.txt` — `Sitemap:` 라인 포함
- `<INDEXNOW_KEY>.txt` — IndexNow 키 파일(루트)
- 메인페이지 `<head>` 에 네이버 사이트 소유확인 메타 태그

**빠른 색인 절차**

1. **빙·네이버·얀덱스(IndexNow)** — 배포가 끝나(키 파일이 도메인에서 열리면) 한 번 실행:
   ```bash
   python3 tools/indexnow.py            # sitemap 전체 통보
   python3 tools/indexnow.py <글 URL>   # 새 글 1건만 즉시 통보
   ```
2. **네이버 서치어드바이저** — 사이트 등록 후 `sitemap.xml` 과 `rss.xml` 제출. 소유확인 메타는 이미 메인에 포함.
3. **구글** — Search Console에서 `sitemap.xml` 제출 + 주요 URL은 URL 검사 → 색인 요청.
   - 참고: 구글은 IndexNow에 참여하지 않으며, 일반 페이지용 즉시 색인 공개 API가 없습니다(Indexing API는 공식적으로 JobPosting/방송 이벤트 전용). sitemap ping 엔드포인트도 폐지되어, 구글은 sitemap + Search Console이 정석입니다.
