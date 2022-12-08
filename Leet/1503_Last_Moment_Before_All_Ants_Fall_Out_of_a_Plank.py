"""
💡✅ GOOD re-state
Tag: Math, Medium, GOOGLE
Lookback:
- beautiful Polya re-state
- lazy at plan, messy in impl.
Similar:
- 1706. Where will the ball fall
"""

import math
from collections import defaultdict
from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        def os_restate():
            """
            Runtime: 199 ms, faster than 43.08% of Python3 online submissions for Last Moment Before All Ants Fall Out of a Plank.

            """
            l = -1 if not left else max(left)
            r = n if not right else min(right)
            return max(l, n - r)

        def fxr_simu():
            """
            TLE: 137 / 167 test cases passed.

            n=3305, left=[...], right=[...]
            """
            cur = defaultdict(list)  # [[dir,clk]]
            for i in left:
                cur[i].append(-1)
            for i in right:
                cur[i].append(1)
            t = 0

            while cur:
                # print(t, '\t', cur)

                nxt = defaultdict(list)
                for p in sorted(list(cur)):
                    # meet/reverse, update
                    if len(cur[p]) == 2:
                        nxt[p + 0.5].append(1)
                        nxt[p - 0.5].append(-1)

                    # regular update
                    else:
                        if cur[p]:
                            d = cur[p].pop()
                            # remove out
                            if p == 0 and d == -1:
                                # noop
                                continue
                            elif p == n and d == 1:
                                # noop
                                continue
                            else:
                                nxt[p + d * 0.5].append(d)

                cur = nxt
                t += 0.5
            return math.floor(t - 0.1)

        # return fxr_simu()
        return os_restate()


sl = Solution()
# print(sl.getLastMoment(n=4, left=[4, 3], right=[0, 1]))
print(sl.getLastMoment(n=7, left=[], right=[0]))

print(
    sl.getLastMoment(
        3305,
        left=[
            2128,
            2765,
            1749,
            145,
            3001,
            166,
            1514,
            1015,
            494,
            1967,
            2911,
            2527,
            3220,
            996,
            2664,
            3167,
            2933,
            229,
            1035,
            2015,
            2418,
            1271,
            2830,
            2502,
            479,
            283,
            628,
            1293,
            1934,
            1247,
            1628,
            780,
            3081,
            2943,
            1550,
            1461,
            1179,
            507,
            2629,
            2140,
            1640,
            2732,
            602,
            3097,
            1072,
            486,
            632,
            3242,
            3019,
            974,
            2782,
            39,
            1495,
            177,
            660,
            352,
            689,
            1017,
            2499,
            274,
            2117,
            2759,
            3270,
            831,
            1783,
            1593,
            1552,
            3067,
            1297,
            2699,
            860,
            2108,
            2412,
            2193,
            2089,
            1282,
            2867,
            3139,
            1432,
            3273,
            1889,
            466,
            76,
            2896,
            704,
            1682,
            3157,
            1807,
            787,
            849,
            3212,
            1806,
            1021,
            1442,
            2224,
            2872,
            2317,
            3260,
            681,
            897,
            3093,
            737,
            2613,
            193,
            1173,
            2582,
            803,
            2655,
            1656,
            2005,
            1575,
            2975,
            1904,
            937,
            1507,
            824,
            807,
            1851,
            2348,
            1962,
            2223,
            588,
            764,
            1248,
            2366,
            3216,
            1366,
            3288,
            2639,
            677,
            2604,
            2146,
            1984,
            180,
            363,
            2576,
            3258,
            3148,
            1450,
            2307,
            2751,
            5,
            156,
            1978,
            1738,
            115,
            186,
            1186,
            2900,
            814,
            1384,
            575,
            2986,
            2960,
            1551,
            2026,
            1283,
            2235,
            2712,
            1681,
            3141,
            242,
            154,
            2913,
            325,
            2097,
            151,
            2678,
            595,
            2191,
            1365,
            1539,
            991,
            1026,
            460,
            10,
            3278,
            2360,
            1872,
            1572,
            1129,
            501,
            453,
            1194,
            311,
            2691,
            2396,
            2557,
            2683,
            789,
            2790,
            1766,
            333,
            1417,
            3166,
            30,
            506,
            3077,
            2707,
            2963,
            1639,
            2998,
            1802,
            129,
            2278,
            3265,
            1315,
            403,
            1898,
            1341,
            1147,
            3119,
            1195,
            72,
            1223,
            2073,
            1459,
            1448,
            2632,
            1854,
            844,
            2290,
            2188,
            209,
            2215,
            2996,
            599,
            1310,
            92,
            832,
            1320,
            2928,
            2796,
            1406,
            799,
            1277,
            1591,
            1200,
            2776,
            301,
            932,
            2738,
            1711,
            1976,
            3116,
            1761,
            234,
            1805,
            1148,
            2372,
            2270,
            1629,
            1558,
            248,
            682,
            3115,
            3099,
            2282,
            2518,
            362,
            2706,
            1389,
            1521,
            1973,
            2458,
            190,
            1650,
            2811,
            1958,
            649,
            63,
            1033,
            438,
            2862,
            1504,
            722,
            462,
            1174,
            567,
            1730,
            1221,
            3217,
            2365,
            967,
            2945,
            1012,
            721,
            174,
            3196,
            1016,
            1123,
            2553,
            2498,
            300,
            2300,
            2551,
            1396,
            1788,
            2490,
            1586,
            1660,
            2649,
            3181,
            1411,
            1375,
            510,
            1128,
            671,
            2196,
            941,
            1259,
            3098,
            2673,
            1023,
            120,
            2760,
            2747,
            143,
            1712,
            422,
            2727,
            842,
            1197,
            2332,
            2136,
            1264,
            644,
            1795,
            2095,
            1164,
            3281,
            593,
            2134,
            457,
            2420,
            1759,
            4,
            1055,
            2670,
            2397,
            2627,
            3261,
            2424,
            2116,
            907,
            228,
            2443,
            2377,
            2652,
            3144,
            2054,
            1543,
            629,
            2978,
            1025,
            604,
            720,
            2575,
            1606,
            1704,
            562,
            3109,
            429,
            1231,
            1398,
            2697,
            2585,
            871,
            3292,
            104,
            1305,
            196,
            760,
            2081,
            2297,
            2827,
            1743,
            639,
            1031,
            1279,
            1718,
            2041,
            3126,
            1565,
            56,
            1418,
            1207,
            673,
            2523,
            973,
            448,
            637,
            2690,
            2411,
            312,
            2563,
            609,
            2245,
            2534,
            3004,
            1933,
            1675,
            169,
            3066,
            2260,
            2349,
            2107,
            160,
            3033,
            2053,
            2085,
            237,
            1888,
            24,
            380,
            2600,
            1710,
            527,
            3106,
            1725,
            2688,
            2232,
            1010,
            101,
            2767,
            950,
            404,
            1069,
            2653,
            2892,
            3172,
            1080,
            1229,
            8,
            2907,
            3069,
            2829,
            1860,
            1982,
            1378,
            1892,
            420,
            276,
            1822,
            1061,
            868,
            523,
            1634,
            1631,
            1137,
            985,
            2532,
            386,
            3251,
            1618,
            286,
            1785,
            2743,
            138,
            1734,
            1326,
            775,
            2455,
            57,
            2966,
            1346,
            3024,
            2903,
            1470,
            2965,
            3160,
            3006,
            1928,
            2157,
            1684,
            230,
            2487,
            3293,
            3105,
            2511,
            517,
            2491,
            2488,
            1349,
            3013,
            3082,
            873,
            1168,
            61,
            232,
            1559,
            1042,
            3214,
            1691,
            2078,
            2004,
            2042,
            1687,
            2187,
            3182,
            891,
            1441,
            1169,
            75,
            2750,
            1735,
            1949,
            58,
            2640,
            1884,
            912,
            901,
            568,
            1685,
            887,
            1447,
            139,
            1774,
            1135,
            1509,
            1146,
            2006,
            459,
            2084,
            1942,
            335,
            2651,
            1249,
            1244,
            2137,
            406,
            3147,
            91,
            1370,
            2347,
            1196,
            2656,
            3114,
            432,
            940,
            1490,
            2118,
            852,
            1374,
            922,
            1178,
            2885,
            3057,
            707,
            1755,
            715,
            3184,
            3289,
            488,
            659,
            1404,
            3140,
            2544,
            1879,
            1843,
            748,
            882,
            3087,
            1830,
            2954,
            1564,
            869,
            1717,
            833,
            2219,
            1127,
            1,
            1304,
            619,
            2483,
            112,
            1580,
            2763,
            1661,
            2080,
            3072,
            2115,
            1585,
            779,
            16,
            825,
            1709,
            1512,
            2667,
            393,
            555,
            1706,
            1037,
            2561,
            542,
            2465,
            3129,
            2675,
            1364,
            1987,
            2909,
            348,
            1134,
            1165,
            200,
            1911,
            1082,
            1482,
            1489,
            566,
            1210,
            95,
            2493,
            3201,
            3113,
            841,
            2301,
            191,
            2452,
            731,
            2345,
            1422,
            49,
            2139,
            391,
            1076,
            1227,
            1604,
            2726,
            2306,
            2661,
            1254,
            729,
            2322,
            1782,
            1641,
            634,
            3271,
            2910,
            250,
            2142,
            3060,
            219,
            376,
            2094,
            1601,
            2162,
            2249,
            571,
            1548,
            3256,
            596,
            1256,
            1948,
            587,
            1081,
            3061,
            999,
            2929,
            243,
            948,
            1694,
            2855,
            2067,
            521,
            2168,
            1775,
            2279,
            735,
            3103,
            2659,
            1097,
            3162,
            272,
            284,
            3291,
            3253,
            1568,
            970,
            615,
            2114,
            1215,
            1673,
            1270,
            2200,
            1655,
            1596,
            963,
            2614,
            296,
            672,
            1457,
            1866,
            2077,
            1219,
            2099,
            3279,
            547,
            1263,
            188,
            1074,
            1008,
            1705,
            2281,
            2212,
            2280,
            3218,
            465,
            1237,
            227,
            2781,
            3076,
            413,
            350,
            1327,
            2046,
            1085,
            1446,
            1498,
            783,
            2949,
            1260,
            972,
            152,
            1122,
            444,
            502,
            100,
            1994,
            3062,
            3276,
            2034,
            2451,
            879,
            2151,
            2013,
            1344,
            44,
            2023,
            2516,
            2032,
            801,
            600,
            377,
            2012,
            2090,
            3068,
            1772,
            2408,
            210,
            1837,
            2758,
            2386,
            924,
            3011,
            921,
            2244,
            3290,
            330,
            317,
            2189,
            218,
            2066,
            812,
            3084,
            2003,
            500,
            1328,
            2500,
            378,
            1240,
            1502,
            3026,
            1531,
            1030,
            1546,
            2248,
            2153,
            2746,
            2344,
            1004,
            2255,
            836,
            102,
            1944,
            254,
            499,
            381,
            123,
            3241,
            1698,
            2206,
            1335,
            1998,
            467,
            2218,
            1020,
            548,
            1819,
            2825,
            2953,
            1764,
            2011,
            2755,
            1666,
            2680,
            1133,
            2131,
            1291,
            777,
            1393,
            339,
            2040,
            953,
            2905,
            691,
            647,
            1878,
            2158,
            914,
            1752,
            2505,
            3037,
            1088,
            3215,
            125,
            338,
            480,
            62,
            667,
            418,
            2489,
            2709,
            1439,
            179,
            270,
            341,
            2165,
            2816,
            728,
            1380,
            732,
            464,
            1787,
            481,
            1599,
            923,
            1540,
            538,
            159,
            94,
            2716,
            2757,
            262,
            988,
            1630,
            33,
            452,
            2525,
            1723,
            2715,
        ],
        right=[
            3224,
            2110,
            1395,
            2874,
            1908,
            3187,
            2695,
            347,
            1556,
            1890,
            1095,
            2860,
            1392,
            2977,
            1965,
            2623,
            3151,
            1835,
            2088,
            3064,
            2010,
            375,
            149,
            412,
            603,
            2243,
            884,
            1695,
            1367,
            2174,
            52,
            3296,
            3225,
            1000,
            2343,
            2475,
            1654,
            2990,
            165,
            2568,
            2536,
            1144,
            2791,
            74,
            322,
            1874,
            1747,
            2208,
            1708,
            38,
            1954,
            1345,
            1535,
            398,
            2596,
            1757,
            875,
            256,
            1719,
            118,
            3053,
            2048,
            906,
            2696,
            2630,
            613,
            1274,
            1537,
            2147,
            3111,
            1435,
            3045,
            1483,
            2425,
            1587,
            328,
            1407,
            2029,
            2856,
            3180,
            2252,
            1083,
            1294,
            473,
            2044,
            1600,
            2778,
            3300,
            2530,
            1034,
            1458,
            2267,
            3168,
            110,
            1917,
            1768,
            1876,
            1728,
            1875,
            1325,
            3146,
            146,
            830,
            1057,
            2123,
            532,
            99,
            2880,
            80,
            1302,
            1703,
            390,
            2737,
            900,
            3014,
            2127,
            709,
            2469,
            2686,
            822,
            1900,
            361,
            977,
            1160,
            443,
            2313,
            224,
            1077,
            2641,
            1871,
            1505,
            2921,
            846,
            1440,
            329,
            519,
            3207,
            495,
            656,
            2476,
            1611,
            1117,
            2087,
            3189,
            1002,
            3252,
            1803,
            1754,
            1211,
            1753,
            2828,
            1424,
            3209,
            1729,
            2588,
            509,
            898,
            528,
            618,
            2126,
            2566,
            2362,
            430,
            27,
            2402,
            3169,
            2735,
            1206,
            238,
            1269,
            2355,
            1014,
            1136,
            1776,
            50,
            1059,
            321,
            2104,
            2161,
            1361,
            773,
            2167,
            829,
            1838,
            2873,
            340,
            2685,
            1533,
            2439,
            1487,
            1428,
            980,
            2293,
            1842,
            2494,
            2926,
            2473,
            1181,
            21,
            589,
            687,
            410,
            1916,
            983,
            2801,
            3089,
            918,
            1454,
            723,
            2486,
            3155,
            1257,
            1663,
            3055,
            1119,
            2724,
            2468,
            204,
            1452,
            14,
            1578,
            2893,
            2555,
            411,
            1018,
            3074,
            762,
            1692,
            1779,
            2434,
            1162,
            2877,
            3059,
            1910,
            1957,
            3227,
            51,
            126,
            2001,
            343,
            1497,
            490,
            257,
            1387,
            2901,
            1333,
            2937,
            368,
            1858,
            1737,
            610,
            1488,
            2030,
            951,
            1028,
            2294,
            3267,
            2539,
            1696,
            34,
            1861,
            543,
            316,
            1676,
            2092,
            2672,
            2863,
            259,
            414,
            2438,
            1726,
            2868,
            127,
            3206,
            997,
            614,
            1205,
            2233,
            40,
            2774,
            1931,
            2444,
            3010,
            2669,
            1913,
            2096,
            1038,
            1353,
            2717,
            1636,
            3142,
            1598,
            2938,
            113,
            746,
            1602,
            2927,
            3238,
            3122,
            31,
            189,
            690,
            32,
            45,
            896,
            344,
            1778,
            2143,
            1336,
            1199,
            2022,
            314,
            20,
            2333,
            1999,
            463,
            556,
            3040,
            489,
            1932,
            817,
            308,
            2850,
            1952,
            1750,
            1467,
            2671,
            3016,
            1177,
            2262,
            795,
            2991,
            546,
            976,
            3054,
            583,
            834,
            895,
            2497,
            2866,
            653,
            1465,
            1937,
            2263,
            758,
            1067,
            2057,
            881,
            915,
            1677,
            513,
            944,
            279,
            2560,
            1964,
            2356,
            2890,
            83,
            1833,
            1877,
            2935,
            1471,
            1794,
            680,
            805,
            55,
            183,
            2457,
            2326,
            2406,
            327,
            427,
            2007,
            1921,
            850,
            2225,
            3294,
            2887,
            2055,
            1331,
            636,
            741,
            1171,
            969,
            3297,
            3174,
            1553,
            25,
            1006,
            287,
            1724,
            484,
            565,
            883,
            903,
            1947,
            1609,
            716,
            65,
            577,
            2802,
            1756,
            2625,
            1268,
            1214,
            1918,
            2422,
            2899,
            1825,
            530,
            3299,
            2703,
            1992,
            2113,
            1607,
            1112,
            1940,
            1810,
            2809,
            2595,
            3003,
            2948,
            1662,
            2368,
            622,
            212,
            1643,
            144,
            2150,
            67,
            3120,
            1856,
            2749,
            718,
            2159,
            2864,
            889,
            1733,
            1518,
            652,
            1212,
            1111,
            1003,
            1001,
            2268,
            1492,
            469,
            1494,
            2070,
            1427,
            2788,
            2982,
            1071,
            371,
            2171,
            2395,
            2257,
            2835,
            2660,
            1950,
            43,
            1901,
            2304,
            2510,
            2292,
            1920,
            2851,
            2122,
            655,
            1647,
            2209,
            2898,
            382,
            2537,
            874,
            2886,
            1781,
            1266,
            520,
            85,
            477,
            1924,
            2098,
            299,
            1975,
            701,
            759,
            2783,
            2201,
            1503,
            3263,
            2917,
            1437,
            1253,
            2624,
            2775,
            2665,
            211,
            1583,
            397,
            2754,
            1657,
            2216,
            3185,
            1633,
            710,
            3131,
            657,
            1047,
            137,
            3158,
            2730,
            3230,
            913,
            2971,
            835,
            2485,
            1319,
            886,
            749,
            2240,
            2983,
            2133,
            1891,
            1659,
            372,
            2351,
            246,
            1426,
            1679,
            253,
            1651,
            342,
            275,
            616,
            857,
            2025,
            692,
            1902,
            1287,
            1496,
            498,
            2871,
            2598,
            456,
            3110,
            1039,
            2079,
            2741,
            2274,
            2531,
            955,
            2517,
            1091,
            2509,
            1232,
            278,
            1678,
            3051,
            1863,
            2720,
            2577,
            1608,
            1622,
            574,
            2700,
            1170,
            3239,
            2994,
            1202,
            291,
            624,
            3101,
            2838,
            1905,
            646,
            631,
            1323,
            1853,
            2160,
            1988,
            1098,
            1612,
            2958,
            3234,
            1478,
            2617,
            1009,
            635,
            22,
            2082,
            1996,
            754,
            505,
            800,
            109,
            1350,
            2766,
            1832,
            536,
            1303,
            1589,
            508,
            1815,
            2636,
            2679,
            2401,
            474,
            3149,
            752,
            358,
            1907,
            3222,
            1799,
            820,
            3143,
            1859,
            1382,
            15,
            2916,
            786,
            1464,
            2508,
            962,
            365,
            1261,
            1172,
            3173,
            1343,
            2495,
            116,
            2394,
            740,
            2059,
            198,
            1513,
            862,
            367,
            114,
            309,
            1665,
            111,
            890,
            1906,
            2818,
            78,
            2902,
            626,
            2496,
            1060,
            1265,
            2843,
            2363,
            249,
            625,
            493,
            1245,
            2723,
            2027,
            2594,
            2056,
            2976,
            2198,
            1786,
            2805,
            1789,
            1295,
            3052,
            979,
            755,
            2353,
            3159,
            3186,
            698,
            421,
            1839,
            2459,
            2464,
            3108,
            1816,
            605,
            2800,
            798,
            3043,
            2806,
            1158,
            2519,
            2919,
            3023,
            2016,
            201,
            3063,
            1369,
            514,
            2190,
            2515,
            1152,
            2756,
            2370,
            2,
            1116,
            1515,
            2881,
            2612,
            394,
            2129,
            1140,
            2572,
            717,
            638,
            1193,
            1862,
            1289,
            47,
            2693,
            888,
            2359,
            1727,
            3134,
            3231,
            2432,
            1118,
            839,
            2284,
            1151,
            843,
            2470,
            2367,
            2178,
            292,
            2214,
            2358,
            909,
            2615,
            1235,
            663,
            2145,
            2413,
            1882,
            1744,
            1252,
            1405,
            2884,
            2442,
            1372,
            2340,
            2341,
            1834,
            3208,
            594,
            1562,
            2812,
            2930,
            3243,
            475,
            2102,
            2477,
            3255,
            2002,
            2462,
            1362,
            1022,
            3277,
            2456,
            326,
            69,
            545,
            2798,
            458,
            2955,
            1434,
            79,
            3127,
            223,
            37,
            1338,
            1433,
            2407,
            2876,
            2821,
            2554,
            2865,
            984,
            1974,
            784,
            245,
            1746,
            1841,
            1423,
            2813,
            703,
            525,
            2185,
            848,
            3176,
            1985,
            2570,
            2043,
            2895,
            2210,
            2480,
            3017,
            1517,
            1125,
            3012,
            2841,
            1316,
            294,
            544,
            415,
            3177,
            928,
            806,
            2984,
            346,
            1166,
            1185,
            440,
            2814,
            178,
            2327,
            82,
            3213,
            1105,
            1528,
            987,
            1983,
            290,
            2258,
            1927,
            133,
            1379,
            3078,
            1236,
            3123,
            3250,
            1826,
            2330,
            1603,
            273,
            2318,
            2448,
            1476,
            1192,
            297,
            1314,
            472,
            975,
            268,
            471,
            522,
            818,
            1955,
            2815,
            1460,
            2538,
            60,
            2581,
            1576,
            2959,
            2120,
            2390,
            2646,
        ],
    )
)
