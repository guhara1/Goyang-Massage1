# 전체 페이지 목록 집계 — 고양 출장마사지·홈타이
from . import main, districts, dongs, stations, areas, info, about

PAGES = (
    [main.PAGE]
    + districts.PAGES
    + dongs.PAGES
    + stations.PAGES
    + areas.PAGES
    + info.PAGES
    + [about.PAGE]
)
