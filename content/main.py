# 메인 페이지 — 고양시 허브. 모든 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY
from .pricing import PRICING

_JSONLD = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{BRAND}",
  "telephone": "{PHONE}",
  "url": "{BASE_URL}/",
  "image": "{BASE_URL}/assets/og-image.png",
  "description": "고양시 전지역 방문 출장마사지·홈타이 예약 안내",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "경기도 고양시"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "고양시 출장마사지·홈타이 지역별 예약 안내",
  "url": "{BASE_URL}/",
  "inLanguage": "ko-KR",
  "primaryImageOfPage": "{BASE_URL}/assets/og-image.png"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "고양시 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "덕양구, 일산동구, 일산서구 3개 구를 기준으로 안내하며, 정확한 가능 여부는 예약 시 위치와 시간으로 확인합니다. 고봉동·관산동 등 외곽은 차량 이동 기준이 달라질 수 있습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "화정1동·행신2동처럼 번호 동도 따로 페이지가 있나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "번호 행정동은 화정동·행신동 같은 대표동 페이지에서 통합 안내하여 중복 페이지를 만들지 않습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "대화역·정발산역 같은 역 인근도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "주요 역세권은 역 상세 페이지에서 인근 생활권과 함께 안내합니다. 환승역도 역명 기준 1개 페이지로 운영합니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Spa · 고양시 전지역</p>
    <h1>고양 출장마사지·홈타이<br>지역별 예약 안내</h1>
    <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 프리미엄 방문 관리.<br>덕양구·일산동구·일산서구 어디든 전화 한 통이면 예약이 끝납니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/reservation/">예약 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>3개 구</strong><span>덕양·일산동·일산서</span></li>
      <li><strong>30개</strong><span>대표동 안내</span></li>
      <li><strong>16개</strong><span>역세권 안내</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section id="intro">
<h2>고양시에서 출장마사지를 찾을 때 먼저 확인할 기준</h2>
<p>고양시 출장마사지를 찾는 분들은 보통 현재 위치에서 가까운 방문 가능 지역을 먼저 확인합니다. 고양시는 덕양구, 일산동구, 일산서구 3개 구로 나뉘며, 일산신도시와 일산호수공원 주변, 킨텍스와 대화역 중심, 화정과 행신을 중심으로 한 덕양구 생활권, 삼송과 원흥·지축으로 이어지는 북동부 생활권이 함께 있는 넓은 지역입니다. 그래서 이 사이트는 "고양 전지역 가능"만 반복하는 대신 구별·대표동별·역세권별로 나누어 안내합니다. 홈타이 역시 자택·숙소·사무실 인근에서 예약 가능 여부를 확인한 뒤 이용하는 방문형 관리 서비스이므로, 정확한 위치와 시간을 기준으로 안내드립니다. 더 자세한 내용은 아래 각 영역의 상세 페이지에서 확인하실 수 있습니다.</p>
</section>

<section id="districts">
<h2>덕양구·일산동구·일산서구 생활권 차이</h2>
<p>덕양구는 화정·행신 같은 역세권 주거지부터 삼송·원흥 신도시, 고양동·관산동 외곽까지 생활권이 넓게 퍼져 있습니다. 일산동구는 백석·마두·정발산·장항·식사·중산·풍산 생활권이 중심이고, 일산서구는 대화·주엽·일산·탄현·덕이·가좌 생활권이 중심입니다. 같은 고양시라도 구마다 주거 형태와 이동 기준이 달라, 구별 안내에서 차이를 먼저 확인하시는 편이 좋습니다.</p>
<ul class="card-grid">
<li><a href="/gyeonggi/goyang/deogyang-gu/">덕양구</a></li>
<li><a href="/gyeonggi/goyang/ilsandong-gu/">일산동구</a></li>
<li><a href="/gyeonggi/goyang/ilsanseo-gu/">일산서구</a></li>
</ul>
<p>3개 구의 전체 구성은 <a href="/gyeonggi/goyang/districts/">구별 안내</a>에서, 행정동 전체 목록은 <a href="/gyeonggi/goyang/dong/">지역별 안내</a>에서 한눈에 확인하실 수 있습니다.</p>
</section>

<section id="dongs">
<h2>대표동별 방문 가능 지역 안내</h2>
<p>대표동 페이지는 화정동, 행신동, 삼송동, 백석동, 마두동, 정발산동, 장항동, 대화동, 주엽동, 일산동, 탄현동 같은 세부 검색을 담당합니다. 번호 행정동(화정1·2동, 행신1~4동, 백석1·2동 등)은 각각 만들지 않고 대표동 페이지 안에서 세부 생활권으로 설명해 중복을 줄였습니다. 거주하시거나 머무시는 동을 선택해 주세요.</p>
<ul class="card-grid">
<li><a href="/gyeonggi/goyang/deogyang-gu/hwajeong-dong/">화정동</a></li>
<li><a href="/gyeonggi/goyang/deogyang-gu/haengsin-dong/">행신동</a></li>
<li><a href="/gyeonggi/goyang/deogyang-gu/samsong-dong/">삼송동</a></li>
<li><a href="/gyeonggi/goyang/ilsandong-gu/baekseok-dong/">백석동</a></li>
<li><a href="/gyeonggi/goyang/ilsandong-gu/madu-dong/">마두동</a></li>
<li><a href="/gyeonggi/goyang/ilsandong-gu/jeongbalsan-dong/">정발산동</a></li>
<li><a href="/gyeonggi/goyang/ilsandong-gu/janghang-dong/">장항동</a></li>
<li><a href="/gyeonggi/goyang/ilsanseo-gu/daehwa-dong/">대화동</a></li>
<li><a href="/gyeonggi/goyang/ilsanseo-gu/juyeop-dong/">주엽동</a></li>
<li><a href="/gyeonggi/goyang/ilsanseo-gu/ilsan-dong/">일산동</a></li>
<li><a href="/gyeonggi/goyang/ilsanseo-gu/tanhyeon-dong/">탄현동</a></li>
</ul>
</section>

<section id="stations">
<h2>대화역·정발산역·백석역·화정역·삼송역 역세권 안내</h2>
<p>역세권 페이지는 대화역, 주엽역, 정발산역, 백석역, 마두역, 화정역, 삼송역, 행신역처럼 실제 검색 수요가 생길 수 있는 위치를 담당합니다. 대곡역·백석역·정발산역 같은 환승역도 역명 기준 1개 페이지로만 운영하고, 지축역은 서울·고양 경계 성격이 있어 삼송·효자·지축 인접 생활권으로 안내합니다.</p>
<ul class="card-grid">
<li><a href="/gyeonggi/goyang/station/daehwa-station/">대화역</a></li>
<li><a href="/gyeonggi/goyang/station/jeongbalsan-station/">정발산역</a></li>
<li><a href="/gyeonggi/goyang/station/baekseok-station/">백석역</a></li>
<li><a href="/gyeonggi/goyang/station/madu-station/">마두역</a></li>
<li><a href="/gyeonggi/goyang/station/hwajeong-station/">화정역</a></li>
<li><a href="/gyeonggi/goyang/station/samsong-station/">삼송역</a></li>
<li><a href="/gyeonggi/goyang/station/haengsin-station/">행신역</a></li>
<li><a href="/gyeonggi/goyang/station/juyeop-station/">주엽역</a></li>
</ul>
<p>16개 역세권 전체는 <a href="/gyeonggi/goyang/station/">역세권 안내</a>에서, 호수공원·킨텍스·라페스타 같은 거점은 <a href="/gyeonggi/goyang/area/">생활권 안내</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="areas">
<h2>일산호수공원·킨텍스·라페스타 거점 생활권 안내</h2>
<p>생활권 페이지는 행정동 검색과 의도가 다른 거점을 담당합니다. 일산호수공원 생활권은 공원 인접 주거·상권을, 라페스타·웨스턴돔 생활권은 정발산·장항 상권을, 킨텍스·대화 생활권은 전시장과 숙소 중심을 설명합니다. 같은 대화동이라도 일반 지역 페이지와 거점 생활권 페이지의 역할을 다르게 잡아 중복을 줄였습니다.</p>
<ul class="card-grid">
<li><a href="/gyeonggi/goyang/area/ilsan-lake-park/">일산호수공원</a></li>
<li><a href="/gyeonggi/goyang/area/lafesta-western-dom/">라페스타·웨스턴돔</a></li>
<li><a href="/gyeonggi/goyang/area/kintex-daehwa/">킨텍스·대화</a></li>
<li><a href="/gyeonggi/goyang/area/baekseok-madu/">백석·마두</a></li>
<li><a href="/gyeonggi/goyang/area/hwajeong-cityhall/">화정·고양시청</a></li>
<li><a href="/gyeonggi/goyang/area/samsong-wonheung/">삼송·원흥</a></li>
</ul>
</section>

<section id="hometai">
<h2>고양시 홈타이 예약 전 확인사항</h2>
<p>고양시 홈타이 예약 전에는 방문 가능 지역, 예약 가능 시간, 추가 이동비, 결제 방식, 취소 기준, 개인정보 처리 기준을 먼저 확인하셔야 합니다. 일산신도시와 화정역, 삼송역처럼 접근성이 좋은 지역도 있지만 고봉동, 관산동, 고양동, 대덕동, 가좌동 일부는 시간대에 따라 차량 이동 기준이 달라질 수 있습니다. 출장마사지와 홈타이의 차이, 처음 이용 시 준비사항은 <a href="/hometai/">홈타이 이용 가이드</a>에서, 예약 절차는 <a href="/reservation/">예약 안내</a>에서, 자택·숙소·사무실별 확인사항은 <a href="/guide/">이용 전 확인사항</a>에서 정리했습니다.</p>
</section>

<section id="policy">
<h2>고양시 페이지 중복 방지 운영 기준</h2>
<p>이 사이트는 검색 순위를 위해 비슷한 페이지를 양산하지 않습니다. 삼송1·2동, 성사1·2동, 화정1·2동, 행신1~4동, 백석1·2동, 마두1·2동, 일산1~3동, 주엽1·2동 같은 번호 동은 대표동으로 통합하고, 환승역은 노선별로 쪼개지 않으며, 예정역·미개통역은 단독 색인 페이지로 만들지 않습니다. 지역명만 바꾼 문장 대신 동·역·생활권마다 고유한 정보를 담는 것이 운영 원칙입니다. 자세한 작성 기준과 책임 주체는 <a href="/about/">사이트 소개</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="howto">
<h2>고양시 출장마사지 사이트 이용 방법</h2>
<p>메인페이지는 고양 전체 안내를 담당하고, 덕양구·일산동구·일산서구 페이지는 구별 생활권 차이를 설명합니다. 대표동 페이지는 세부 동 검색을, 역세권 페이지는 대화역·정발산역·백석역·화정역·삼송역 같은 위치 검색을, 생활권 페이지는 호수공원·킨텍스·라페스타 같은 거점 검색을 담당합니다. 위치 기준이 편하면 지역·역 페이지를, 관리 목적이 먼저 궁금하면 홈타이 이용 가이드를 보신 뒤 예약 전화에서 위치와 시간을 알려주시면 됩니다.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>고양시 전지역 방문이 가능한가요?</h3>
<p>덕양구, 일산동구, 일산서구 3개 구를 기준으로 안내하며, 정확한 가능 여부는 예약 시 위치와 시간으로 확인합니다. 고봉동·관산동 등 외곽은 차량 이동 기준이 달라질 수 있습니다.</p>
</div>
<div class="faq-item">
<h3>화정1동·행신2동처럼 번호 동도 따로 페이지가 있나요?</h3>
<p>번호 행정동은 화정동·행신동 같은 대표동 페이지에서 통합 안내하여 중복 페이지를 만들지 않습니다.</p>
</div>
<div class="faq-item">
<h3>대화역·정발산역 같은 역 인근도 가능한가요?</h3>
<p>주요 역세권은 역 상세 페이지에서 인근 생활권과 함께 안내합니다. 환승역도 역명 기준 1개 페이지로 운영합니다.</p>
</div>
<div class="faq-item">
<h3>당일 예약도 가능한가요?</h3>
<p>가능할 수 있지만 저녁 시간대와 주말은 문의가 몰릴 수 있어 사전 예약을 권장합니다.</p>
</div>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>고양시 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "고양시 출장마사지 | 일산·화정·행신·삼송 홈타이 지역 안내",
    "desc": "고양시 출장마사지·홈타이 예약 전 일산, 화정, 행신, 삼송, 백석, 대화 생활권을 확인하세요.",
    "h1": "고양시 출장마사지 · 고양시 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
