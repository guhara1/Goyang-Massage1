# 사이트 공통 설정 — 고양 출장마사지·홈타이 안내
# 배포 도메인: Cloudflare Pages
BASE_URL = "https://goyang-massage1.pages.dev"

BRAND = "바로 GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 외부 문의(텔레그램) — 푸터 오렌지 버튼
TELEGRAM_SITE = "https://t.me/googleseolab"   # 웹사이트 제작문의
TELEGRAM_BIZ = "https://t.me/googleseolab"    # 제휴문의

# IndexNow 키 — 빙·네이버·얀덱스 즉시 색인 통보용.
# 빌드 시 루트에 "<INDEXNOW_KEY>.txt" 파일이 생성되며, 그 내용은 키와 동일해야 한다.
INDEXNOW_KEY = "8f2c4a9e7b1d4e6fa3c5b8d201e9f7a4"

# ── 지역 데이터(단일 소스) ───────────────────────────────
# 메뉴·URL 에는 "출장마사지" 키워드를 반복하지 않는다. 지역명만 사용한다.

DISTRICTS = [
    ("deogyang-gu", "덕양구"),
    ("ilsandong-gu", "일산동구"),
    ("ilsanseo-gu", "일산서구"),
]

# (slug, 이름, 구 slug) — 번호 행정동은 대표동으로 통합한다.
DONGS = [
    # 덕양구 (15)
    ("jugyo-dong", "주교동", "deogyang-gu"),
    ("wonsin-dong", "원신동", "deogyang-gu"),
    ("heungdo-dong", "흥도동", "deogyang-gu"),
    ("seongsa-dong", "성사동", "deogyang-gu"),
    ("hyoja-dong", "효자동", "deogyang-gu"),
    ("samsong-dong", "삼송동", "deogyang-gu"),
    ("changneung-dong", "창릉동", "deogyang-gu"),
    ("goyang-dong", "고양동", "deogyang-gu"),
    ("gwansan-dong", "관산동", "deogyang-gu"),
    ("neunggok-dong", "능곡동", "deogyang-gu"),
    ("hwajeong-dong", "화정동", "deogyang-gu"),
    ("haengju-dong", "행주동", "deogyang-gu"),
    ("haengsin-dong", "행신동", "deogyang-gu"),
    ("hwajeon-dong", "화전동", "deogyang-gu"),
    ("daedeok-dong", "대덕동", "deogyang-gu"),
    # 일산동구 (8)
    ("siksa-dong", "식사동", "ilsandong-gu"),
    ("jungsan-dong", "중산동", "ilsandong-gu"),
    ("jeongbalsan-dong", "정발산동", "ilsandong-gu"),
    ("pungsan-dong", "풍산동", "ilsandong-gu"),
    ("baekseok-dong", "백석동", "ilsandong-gu"),
    ("madu-dong", "마두동", "ilsandong-gu"),
    ("janghang-dong", "장항동", "ilsandong-gu"),
    ("gobong-dong", "고봉동", "ilsandong-gu"),
    # 일산서구 (7)
    ("ilsan-dong", "일산동", "ilsanseo-gu"),
    ("tanhyeon-dong", "탄현동", "ilsanseo-gu"),
    ("juyeop-dong", "주엽동", "ilsanseo-gu"),
    ("daehwa-dong", "대화동", "ilsanseo-gu"),
    ("songpo-dong", "송포동", "ilsanseo-gu"),
    ("deogi-dong", "덕이동", "ilsanseo-gu"),
    ("gajwa-dong", "가좌동", "ilsanseo-gu"),
]

# (slug, 이름) — 환승역도 URL 하나만. 예정역·미개통역은 만들지 않는다.
STATIONS = [
    ("daehwa-station", "대화역"),
    ("juyeop-station", "주엽역"),
    ("jeongbalsan-station", "정발산역"),
    ("madu-station", "마두역"),
    ("baekseok-station", "백석역"),
    ("daegok-station", "대곡역"),
    ("hwajeong-station", "화정역"),
    ("wondang-station", "원당역"),
    ("samsong-station", "삼송역"),
    ("jichuk-nearby-area", "지축역 인접 생활권"),
    ("haengsin-station", "행신역"),
    ("neunggok-station", "능곡역"),
    ("ilsan-station", "일산역"),
    ("tanhyeon-station", "탄현역"),
    ("pungsan-station", "풍산역"),
    ("baengma-station", "백마역"),
]

# (slug, 이름)
AREAS = [
    ("ilsan-lake-park", "일산호수공원 생활권"),
    ("lafesta-western-dom", "라페스타·웨스턴돔 생활권"),
    ("kintex-daehwa", "킨텍스·대화 생활권"),
    ("baekseok-madu", "백석·마두 생활권"),
    ("siksa-wicity", "식사·위시티 생활권"),
    ("juyeop-ilsan-newtown", "주엽·일산신도시 생활권"),
    ("tanhyeon-deogi", "탄현·덕이 생활권"),
    ("hwajeong-cityhall", "화정·고양시청 생활권"),
    ("haengsin-neunggok", "행신·능곡 생활권"),
    ("samsong-wonheung", "삼송·원흥 생활권"),
    ("wondang-seongsa", "원당·성사 생활권"),
    ("jichuk-changneung", "지축·창릉 인접 생활권"),
    ("hyangdong-deogeun", "향동·덕은 생활권"),
    ("goyang-gwansan", "고양동·관산 생활권"),
]

GOYANG_BASE = "/gyeonggi/goyang"


def dong_url(slug):
    for s, _name, d in DONGS:
        if s == slug:
            return f"{GOYANG_BASE}/{d}/{slug}/"
    raise KeyError(slug)


def station_url(slug):
    return f"{GOYANG_BASE}/station/{slug}/"


def area_url(slug):
    return f"{GOYANG_BASE}/area/{slug}/"


def district_url(slug):
    return f"{GOYANG_BASE}/{slug}/"


# ── 상단 메뉴 ─────────────────────────────────────────────
# 하위 메뉴에는 키워드를 반복하지 않고 지역명·역명만 표시한다.
NAV = [
    ("홈", "/", []),
    ("구별 안내", f"{GOYANG_BASE}/districts/", [
        ("덕양구", "/gyeonggi/goyang/deogyang-gu/"),
        ("일산동구", "/gyeonggi/goyang/ilsandong-gu/"),
        ("일산서구", "/gyeonggi/goyang/ilsanseo-gu/"),
    ]),
    ("지역별 안내", f"{GOYANG_BASE}/dong/", [
        ("덕양구 지역", "/gyeonggi/goyang/deogyang-gu/"),
        ("일산동구 지역", "/gyeonggi/goyang/ilsandong-gu/"),
        ("일산서구 지역", "/gyeonggi/goyang/ilsanseo-gu/"),
        ("화정동", "/gyeonggi/goyang/deogyang-gu/hwajeong-dong/"),
        ("행신동", "/gyeonggi/goyang/deogyang-gu/haengsin-dong/"),
        ("삼송동", "/gyeonggi/goyang/deogyang-gu/samsong-dong/"),
        ("백석동", "/gyeonggi/goyang/ilsandong-gu/baekseok-dong/"),
        ("마두동", "/gyeonggi/goyang/ilsandong-gu/madu-dong/"),
        ("정발산동", "/gyeonggi/goyang/ilsandong-gu/jeongbalsan-dong/"),
        ("장항동", "/gyeonggi/goyang/ilsandong-gu/janghang-dong/"),
        ("대화동", "/gyeonggi/goyang/ilsanseo-gu/daehwa-dong/"),
        ("주엽동", "/gyeonggi/goyang/ilsanseo-gu/juyeop-dong/"),
        ("일산동", "/gyeonggi/goyang/ilsanseo-gu/ilsan-dong/"),
        ("탄현동", "/gyeonggi/goyang/ilsanseo-gu/tanhyeon-dong/"),
    ]),
    ("역세권 안내", f"{GOYANG_BASE}/station/", [
        ("역 전체", "/gyeonggi/goyang/station/"),
        ("대화역", "/gyeonggi/goyang/station/daehwa-station/"),
        ("주엽역", "/gyeonggi/goyang/station/juyeop-station/"),
        ("정발산역", "/gyeonggi/goyang/station/jeongbalsan-station/"),
        ("마두역", "/gyeonggi/goyang/station/madu-station/"),
        ("백석역", "/gyeonggi/goyang/station/baekseok-station/"),
        ("대곡역", "/gyeonggi/goyang/station/daegok-station/"),
        ("화정역", "/gyeonggi/goyang/station/hwajeong-station/"),
        ("원당역", "/gyeonggi/goyang/station/wondang-station/"),
        ("삼송역", "/gyeonggi/goyang/station/samsong-station/"),
        ("행신역", "/gyeonggi/goyang/station/haengsin-station/"),
        ("능곡역", "/gyeonggi/goyang/station/neunggok-station/"),
        ("일산역", "/gyeonggi/goyang/station/ilsan-station/"),
        ("탄현역", "/gyeonggi/goyang/station/tanhyeon-station/"),
        ("풍산역", "/gyeonggi/goyang/station/pungsan-station/"),
        ("백마역", "/gyeonggi/goyang/station/baengma-station/"),
    ]),
    ("생활권 안내", f"{GOYANG_BASE}/area/", [
        ("생활권 전체", "/gyeonggi/goyang/area/"),
        ("일산호수공원", "/gyeonggi/goyang/area/ilsan-lake-park/"),
        ("라페스타·웨스턴돔", "/gyeonggi/goyang/area/lafesta-western-dom/"),
        ("킨텍스·대화", "/gyeonggi/goyang/area/kintex-daehwa/"),
        ("백석·마두", "/gyeonggi/goyang/area/baekseok-madu/"),
        ("식사·위시티", "/gyeonggi/goyang/area/siksa-wicity/"),
        ("주엽·일산신도시", "/gyeonggi/goyang/area/juyeop-ilsan-newtown/"),
        ("탄현·덕이", "/gyeonggi/goyang/area/tanhyeon-deogi/"),
        ("화정·고양시청", "/gyeonggi/goyang/area/hwajeong-cityhall/"),
        ("행신·능곡", "/gyeonggi/goyang/area/haengsin-neunggok/"),
        ("삼송·원흥", "/gyeonggi/goyang/area/samsong-wonheung/"),
        ("원당·성사", "/gyeonggi/goyang/area/wondang-seongsa/"),
        ("지축·창릉", "/gyeonggi/goyang/area/jichuk-changneung/"),
        ("향동·덕은", "/gyeonggi/goyang/area/hyangdong-deogeun/"),
        ("고양동·관산", "/gyeonggi/goyang/area/goyang-gwansan/"),
    ]),
    ("예약 안내", "/reservation/", [
        ("예약 가능 지역 확인", "/reservation/#place"),
        ("예약 가능 시간 안내", "/reservation/#hours"),
        ("추가 이동비 안내", "/reservation/#fee"),
        ("결제 방식 안내", "/reservation/#payment"),
        ("예약 변경 안내", "/reservation/#change"),
        ("취소 기준 안내", "/reservation/#cancel"),
    ]),
    ("이용 전 확인사항", "/guide/", [
        ("방문 가능 주소 확인", "/guide/#address"),
        ("자택 이용 전 확인", "/guide/#home"),
        ("숙소 이용 전 확인", "/guide/#hotel"),
        ("사무실 인근 이용 전 확인", "/guide/#office"),
        ("개인정보 처리 기준", "/guide/#privacy"),
        ("고객 안전 안내", "/guide/#safety"),
    ]),
    ("홈타이 이용 가이드", "/hometai/", [
        ("홈타이란?", "/hometai/#what"),
        ("출장마사지와 홈타이 차이", "/hometai/#diff"),
        ("고양시 홈타이 이용 전 기준", "/hometai/#standard"),
        ("지역별 이동 기준", "/hometai/#move"),
        ("추가 비용 확인 기준", "/hometai/#fee"),
        ("처음 이용하는 고객 안내", "/hometai/#first"),
    ]),
    ("고객센터", "/support/", [
        ("자주 묻는 질문", "/support/#faq"),
        ("1:1 문의", "/support/#contact"),
        ("운영 기준", "/support/#policy"),
        ("사이트 소개", "/about/"),
        ("개인정보처리방침", "/support/privacy/"),
        ("이용약관", "/support/terms/"),
    ]),
]
