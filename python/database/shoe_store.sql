--
-- PostgreSQL database dump
--

-- Dumped from database version 17.5
-- Dumped by pg_dump version 17.5

-- Started on 2026-11-13 13:29:39

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 217 (class 1259 OID 25675)
-- Name: order_items; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.order_items (
    order_number integer NOT NULL,
    quantity smallint,
    shoe_id integer NOT NULL
);


ALTER TABLE public.order_items OWNER TO shoe_user;

--
-- TOC entry 218 (class 1259 OID 25678)
-- Name: orders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.orders (
    order_date date,
    delivery_date date,
    user_id integer,
    receive_code integer,
    status character varying(40),
    pickup_point_code integer,
    order_number integer NOT NULL
);


ALTER TABLE public.orders OWNER TO shoe_user;

--
-- TOC entry 219 (class 1259 OID 25681)
-- Name: orders_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.orders_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.orders_id_seq OWNER TO shoe_user;

--
-- TOC entry 4938 (class 0 OID 0)
-- Dependencies: 219
-- Name: orders_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.orders_id_seq OWNED BY public.orders.order_number;


--
-- TOC entry 220 (class 1259 OID 25682)
-- Name: pick-up_points; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."pick-up_points" (
    town character varying(40),
    street character varying(40),
    id integer NOT NULL,
    postal_code bigint,
    house character varying(10)
);


ALTER TABLE public."pick-up_points" OWNER TO shoe_user;

--
-- TOC entry 221 (class 1259 OID 25685)
-- Name: pick-up_points_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."pick-up_points_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."pick-up_points_id_seq" OWNER TO shoe_user;

--
-- TOC entry 4939 (class 0 OID 0)
-- Dependencies: 221
-- Name: pick-up_points_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."pick-up_points_id_seq" OWNED BY public."pick-up_points".id;


--
-- TOC entry 222 (class 1259 OID 25686)
-- Name: shoes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.shoes (
    name character varying(40),
    unit character varying(40),
    price smallint,
    supplier character varying(40),
    manufacturer character varying(40),
    category character varying(40),
    discount smallint,
    quantity_in_stock integer,
    description text,
    image character varying(100),
    id integer NOT NULL,
    article character varying(40)
);


ALTER TABLE public.shoes OWNER TO shoe_user;

--
-- TOC entry 223 (class 1259 OID 25691)
-- Name: shoes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.shoes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.shoes_id_seq OWNER TO shoe_user;

--
-- TOC entry 4940 (class 0 OID 0)
-- Dependencies: 223
-- Name: shoes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.shoes_id_seq OWNED BY public.shoes.id;


--
-- TOC entry 224 (class 1259 OID 25692)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    first_name character varying(40),
    last_name character varying(40),
    patronymic character varying(40),
    login character varying(40),
    password character varying(40),
    status character varying(40)
);


ALTER TABLE public.users OWNER TO shoe_user;

--
-- TOC entry 225 (class 1259 OID 25695)
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO shoe_user;

--
-- TOC entry 4941 (class 0 OID 0)
-- Dependencies: 225
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- TOC entry 4761 (class 2604 OID 25696)
-- Name: orders order_number; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders ALTER COLUMN order_number SET DEFAULT nextval('public.orders_id_seq'::regclass);


--
-- TOC entry 4762 (class 2604 OID 25697)
-- Name: pick-up_points id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."pick-up_points" ALTER COLUMN id SET DEFAULT nextval('public."pick-up_points_id_seq"'::regclass);


--
-- TOC entry 4763 (class 2604 OID 25698)
-- Name: shoes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shoes ALTER COLUMN id SET DEFAULT nextval('public.shoes_id_seq'::regclass);


--
-- TOC entry 4764 (class 2604 OID 25699)
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- TOC entry 4924 (class 0 OID 25675)
-- Dependencies: 217
-- Data for Name: order_items; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.order_items (order_number, quantity, shoe_id) FROM stdin;
92	2	1397
92	2	1398
93	1	1399
93	1	1400
94	10	1401
94	10	1402
95	5	1403
95	4	1404
96	2	1397
96	2	1398
97	1	1399
97	1	1400
98	10	1401
98	10	1402
99	5	1403
99	4	1404
100	5	1405
100	1	1406
101	5	1407
101	5	1408
\.


--
-- TOC entry 4925 (class 0 OID 25678)
-- Dependencies: 218
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.orders (order_date, delivery_date, user_id, receive_code, status, pickup_point_code, order_number) FROM stdin;
2025-02-27	2025-04-20	644	901	Р—Р°РІРµСЂС€РµРЅ	1	92
2022-09-28	2025-04-21	641	902	Р—Р°РІРµСЂС€РµРЅ	11	93
2025-03-21	2025-04-22	642	903	Р—Р°РІРµСЂС€РµРЅ	2	94
2025-02-20	2025-04-23	643	904	Р—Р°РІРµСЂС€РµРЅ	11	95
2025-03-17	2025-04-24	644	905	Р—Р°РІРµСЂС€РµРЅ	2	96
2025-03-01	2025-04-25	641	906	Р—Р°РІРµСЂС€РµРЅ	15	97
\N	2025-04-26	642	907	Р—Р°РІРµСЂС€РµРЅ	3	98
2025-03-31	2025-04-27	643	908	РќРѕРІС‹Р№ 	19	99
2025-04-02	2025-04-28	644	909	РќРѕРІС‹Р№ 	5	100
2025-04-03	2025-04-29	644	910	РќРѕРІС‹Р№ 	19	101
\.


--
-- TOC entry 4927 (class 0 OID 25682)
-- Dependencies: 220
-- Data for Name: pick-up_points; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."pick-up_points" (town, street, id, postal_code, house) FROM stdin;
Рі. Р›РµСЃРЅРѕР№	СѓР». Р’РёС€РЅРµРІР°СЏ	1	420151	32
Рі. Р›РµСЃРЅРѕР№	СѓР». РџРѕРґРіРѕСЂРЅР°СЏ	2	125061	8
Рі. Р›РµСЃРЅРѕР№	СѓР». РЁРѕСЃСЃРµР№РЅР°СЏ	3	630370	24
Рі. Р›РµСЃРЅРѕР№	СѓР». Р—РµР»РµРЅР°СЏ	4	400562	32
Рі. Р›РµСЃРЅРѕР№	СѓР». РњР°СЏРєРѕРІСЃРєРѕРіРѕ	5	614510	47
Рі. Р›РµСЃРЅРѕР№	СѓР». РЎРІРµС‚Р»Р°СЏ	6	410542	46
Рі. Р›РµСЃРЅРѕР№	СѓР». Р¦РІРµС‚РѕС‡РЅР°СЏ	7	620839	8
Рі. Р›РµСЃРЅРѕР№	СѓР». РљРѕРјРјСѓРЅРёСЃС‚РёС‡РµСЃРєР°СЏ	8	443890	1
Рі. Р›РµСЃРЅРѕР№	СѓР». РЎРїРѕСЂС‚РёРІРЅР°СЏ	9	603379	46
Рі. Р›РµСЃРЅРѕР№	СѓР». Р“РѕРіРѕР»СЏ	10	603721	41
Рі. Р›РµСЃРЅРѕР№	СѓР». РЎРµРІРµСЂРЅР°СЏ	11	410172	13
Рі. Р›РµСЃРЅРѕР№	СѓР». РњРѕР»РѕРґРµР¶РЅР°СЏ	12	614611	50
Рі.Р›РµСЃРЅРѕР№	СѓР». РќРѕРІР°СЏ	13	454311	19
Рі.Р›РµСЃРЅРѕР№	СѓР». РћРєС‚СЏР±СЂСЊСЃРєР°СЏ	14	660007	19
Рі. Р›РµСЃРЅРѕР№	СѓР». РЎР°РґРѕРІР°СЏ	15	603036	4
Рі.Р›РµСЃРЅРѕР№	СѓР». Р¤СЂСѓРЅР·Рµ	16	394060	43
Рі. Р›РµСЃРЅРѕР№	СѓР». РЁРєРѕР»СЊРЅР°СЏ	17	410661	50
Рі. Р›РµСЃРЅРѕР№	СѓР». РљРѕРјРјСѓРЅРёСЃС‚РёС‡РµСЃРєР°СЏ	18	625590	20
Рі. Р›РµСЃРЅРѕР№	СѓР». 8 РњР°СЂС‚Р°	19	625683	NaN
Рі.Р›РµСЃРЅРѕР№	СѓР». РљРѕРјСЃРѕРјРѕР»СЊСЃРєР°СЏ	20	450983	26
Рі. Р›РµСЃРЅРѕР№	СѓР». Р§РµС…РѕРІР°	21	394782	3
Рі. Р›РµСЃРЅРѕР№	СѓР». Р”Р·РµСЂР¶РёРЅСЃРєРѕРіРѕ	22	603002	28
Рі. Р›РµСЃРЅРѕР№	СѓР». РќР°Р±РµСЂРµР¶РЅР°СЏ	23	450558	30
Рі. Р›РµСЃРЅРѕР№	СѓР». Р§РµС…РѕРІР°	24	344288	1
Рі.Р›РµСЃРЅРѕР№	СѓР». РЎС‚РµРїРЅР°СЏ	25	614164	30
Рі. Р›РµСЃРЅРѕР№	СѓР». РљРѕРјРјСѓРЅРёСЃС‚РёС‡РµСЃРєР°СЏ	26	394242	43
Рі. Р›РµСЃРЅРѕР№	СѓР». РЎРѕР»РЅРµС‡РЅР°СЏ	27	660540	25
Рі. Р›РµСЃРЅРѕР№	СѓР». РЁРѕСЃСЃРµР№РЅР°СЏ	28	125837	40
Рі. Р›РµСЃРЅРѕР№	СѓР». РџР°СЂС‚РёР·Р°РЅСЃРєР°СЏ	29	125703	49
Рі. Р›РµСЃРЅРѕР№	СѓР». РџРѕР±РµРґС‹	30	625283	46
Рі. Р›РµСЃРЅРѕР№	СѓР». РџРѕР»РµРІР°СЏ	31	614753	35
Рі. Р›РµСЃРЅРѕР№	СѓР». РњР°СЏРєРѕРІСЃРєРѕРіРѕ	32	426030	44
Рі. Р›РµСЃРЅРѕР№ СѓР». РљР»СѓР±РЅР°СЏ	44	33	450375	NaN
Рі. Р›РµСЃРЅРѕР№	СѓР». РќРµРєСЂР°СЃРѕРІР°	34	625560	12
Рі. Р›РµСЃРЅРѕР№	СѓР». РљРѕРјСЃРѕРјРѕР»СЊСЃРєР°СЏ	35	630201	17
Рі. Р›РµСЃРЅРѕР№	СѓР». РњРёС‡СѓСЂРёРЅР°	36	190949	26
\.


--
-- TOC entry 4929 (class 0 OID 25686)
-- Dependencies: 222
-- Data for Name: shoes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.shoes (name, unit, price, supplier, manufacturer, category, discount, quantity_in_stock, description, image, id, article) FROM stdin;
Р‘РѕС‚РёРЅРєРё	С€С‚.	4990	Kari	Kari	Р–РµРЅСЃРєР°СЏ РѕР±СѓРІСЊ	3	6	Р–РµРЅСЃРєРёРµ Р‘РѕС‚РёРЅРєРё РґРµРјРёСЃРµР·РѕРЅРЅС‹Рµ kari	1.jpg	1397	Рђ112Рў4
Р‘РѕС‚РёРЅРєРё	С€С‚.	3244	РћР±СѓРІСЊ РґР»СЏ РІР°СЃ	Marco Tozzi	Р–РµРЅСЃРєР°СЏ РѕР±СѓРІСЊ	2	13	Р‘РѕС‚РёРЅРєРё Marco Tozzi Р¶РµРЅСЃРєРёРµ РґРµРјРёСЃРµР·РѕРЅРЅС‹Рµ, СЂР°Р·РјРµСЂ 39, С†РІРµС‚ Р±РµР¶РµРІС‹Р№	2.jpg	1398	F635R4
РўСѓС„Р»Рё	С€С‚.	4499	Kari	Kari	РњСѓР¶СЃРєР°СЏ РѕР±СѓРІСЊ	4	5	РўСѓС„Р»Рё kari РјСѓР¶СЃРєРёРµ РєР»Р°СЃСЃРёРєР° MYZ21AW-450A, СЂР°Р·РјРµСЂ 43, С†РІРµС‚: С‡РµСЂРЅС‹Р№	3.jpg	1399	H782T5
Р‘РѕС‚РёРЅРєРё	С€С‚.	5900	Kari	Р РѕСЃ	РњСѓР¶СЃРєР°СЏ РѕР±СѓРІСЊ	2	8	РњСѓР¶СЃРєРёРµ Р±РѕС‚РёРЅРєРё Р РѕСЃ-РћР±СѓРІСЊВ РєРѕР¶Р°РЅС‹Рµ СЃ РЅР°С‚СѓСЂР°Р»СЊРЅС‹Рј РјРµС…РѕРј	4.jpg	1400	G783F5
Р‘РѕС‚РёРЅРєРё	С€С‚.	3800	РћР±СѓРІСЊ РґР»СЏ РІР°СЃ	Rieker	РњСѓР¶СЃРєР°СЏ РѕР±СѓРІСЊ	2	16	B3430/14 РџРѕР»СѓР±РѕС‚РёРЅРєРё РјСѓР¶СЃРєРёРµ Rieker	5.jpg	1401	J384T6
РљСЂРѕСЃСЃРѕРІРєРё	С€С‚.	4100	РћР±СѓРІСЊ РґР»СЏ РІР°СЃ	Р РѕСЃ	РњСѓР¶СЃРєР°СЏ РѕР±СѓРІСЊ	3	6	129615-4 РљСЂРѕСЃСЃРѕРІРєРё РјСѓР¶СЃРєРёРµ	6.jpg	1402	D572U8
РўСѓС„Р»Рё	С€С‚.	2700	Kari	Marco Tozzi	Р–РµРЅСЃРєР°СЏ РѕР±СѓРІСЊ	2	14	РўСѓС„Р»Рё Marco Tozzi Р¶РµРЅСЃРєРёРµ Р»РµС‚РЅРёРµ, СЂР°Р·РјРµСЂ 39, С†РІРµС‚ С‡РµСЂРЅС‹Р№	7.jpg	1403	F572H7
РџРѕР»СѓР±РѕС‚РёРЅРєРё	С€С‚.	1890	РћР±СѓРІСЊ РґР»СЏ РІР°СЃ	Alessio Nesca	Р–РµРЅСЃРєР°СЏ РѕР±СѓРІСЊ	4	4	РџРѕР»СѓР±РѕС‚РёРЅРєРё Alessio Nesca Р¶РµРЅСЃРєРёРµ 3-30797-47, СЂР°Р·РјРµСЂ 37, С†РІРµС‚: Р±РѕСЂРґРѕРІС‹Р№	8.jpg	1404	D329H3
РўСѓС„Р»Рё	С€С‚.	4300	Kari	Rieker	Р–РµРЅСЃРєР°СЏ РѕР±СѓРІСЊ	2	6	РўСѓС„Р»Рё Rieker Р¶РµРЅСЃРєРёРµ РґРµРјРёСЃРµР·РѕРЅРЅС‹Рµ, СЂР°Р·РјРµСЂ 41, С†РІРµС‚ РєРѕСЂРёС‡РЅРµРІС‹Р№	9.jpg	1405	B320R5
РўСѓС„Р»Рё	С€С‚.	2800	Kari	Kari	Р–РµРЅСЃРєР°СЏ РѕР±СѓРІСЊ	3	15	РўСѓС„Р»Рё kari Р¶РµРЅСЃРєРёРµ TR-YR-413017, СЂР°Р·РјРµСЂ 37, С†РІРµС‚: С‡РµСЂРЅС‹Р№	10.jpg	1406	G432E4
РџРѕР»СѓР±РѕС‚РёРЅРєРё	С€С‚.	2156	РћР±СѓРІСЊ РґР»СЏ РІР°СЃ	CROSBY	РњСѓР¶СЃРєР°СЏ РѕР±СѓРІСЊ	3	6	407700/01-01 РџРѕР»СѓР±РѕС‚РёРЅРєРё РјСѓР¶СЃРєРёРµ CROSBY	NaN	1407	S213E3
РџРѕР»СѓР±РѕС‚РёРЅРєРё	С€С‚.	1800	Kari	Kari	Р–РµРЅСЃРєР°СЏ РѕР±СѓРІСЊ	2	14	РџРѕР»СѓР±РѕС‚РёРЅРєРё kari Р¶РµРЅСЃРєРёРµ MYZ20S-149, СЂР°Р·РјРµСЂ 41, С†РІРµС‚: С‡РµСЂРЅС‹Р№	NaN	1408	E482R4
РљРµРґС‹	С€С‚.	5500	РћР±СѓРІСЊ РґР»СЏ РІР°СЃ	CROSBY	РњСѓР¶СЃРєР°СЏ РѕР±СѓРІСЊ	3	0	РљРµРґС‹ Caprice РјСѓР¶СЃРєРёРµ РґРµРјРёСЃРµР·РѕРЅРЅС‹Рµ, СЂР°Р·РјРµСЂ 42, С†РІРµС‚ С‡РµСЂРЅС‹Р№	NaN	1409	S634B5
РџРѕР»СѓР±РѕС‚РёРЅРєРё	С€С‚.	2100	РћР±СѓРІСЊ РґР»СЏ РІР°СЃ	CROSBY	РњСѓР¶СЃРєР°СЏ РѕР±СѓРІСЊ	2	3	407700/01-02 РџРѕР»СѓР±РѕС‚РёРЅРєРё РјСѓР¶СЃРєРёРµ CROSBY	NaN	1410	K345R4
РўСѓС„Р»Рё	С€С‚.	5400	РћР±СѓРІСЊ РґР»СЏ РІР°СЃ	Rieker	Р–РµРЅСЃРєР°СЏ РѕР±СѓРІСЊ	4	18	РўСѓС„Р»Рё Р¶РµРЅСЃРєРёРµ РґРµРјРёСЃРµР·РѕРЅРЅС‹Рµ Rieker Р°СЂС‚РёРєСѓР» 55073-68/37	NaN	1411	O754F4
Р‘РѕС‚РёРЅРєРё	С€С‚.	6600	Kari	Kari	Р–РµРЅСЃРєР°СЏ РѕР±СѓРІСЊ	12	9	Р‘РѕС‚РёРЅРєРё Р¶РµРЅСЃРєРёРµ Р·РёРјРЅРёРµ ROMER Р°СЂС‚. 893167-01 Р§РµСЂРЅС‹Р№	NaN	1412	G531F4
РўР°РїРѕС‡РєРё	С€С‚.	500	Kari	Kari	РњСѓР¶СЃРєР°СЏ РѕР±СѓРІСЊ	13	0	РўР°РїРѕС‡РєРё РјСѓР¶СЃРєРёРµ РђСЂС‚.70701-55-67СЃРёРЅ СЂ.41	NaN	1413	J542F5
Р‘РѕС‚РёРЅРєРё	С€С‚.	2700	РћР±СѓРІСЊ РґР»СЏ РІР°СЃ	Rieker	РњСѓР¶СЃРєР°СЏ РѕР±СѓРІСЊ	2	5	РњСѓР¶СЃРєРёРµ РєРѕР¶Р°РЅС‹Рµ Р±РѕС‚РёРЅРєРё/РјСѓР¶СЃРєРёРµ Р±РѕС‚РёРЅРєРё	NaN	1414	B431R5
РўСѓС„Р»Рё	С€С‚.	6800	Kari	CROSBY	Р–РµРЅСЃРєР°СЏ РѕР±СѓРІСЊ	15	15	РўСѓС„Р»Рё Р¶РµРЅСЃРєРёРµ, ARGO, СЂР°Р·РјРµСЂ 38	NaN	1415	P764G4
Р‘РѕС‚РёРЅРєРё	С€С‚.	10200	Kari	Alessio Nesca	Р–РµРЅСЃРєР°СЏ РѕР±СѓРІСЊ	15	9	Р‘РѕС‚РёРЅРєРё Р¶РµРЅСЃРєРёРµ, ARGO, СЂР°Р·РјРµСЂ 40	NaN	1416	C436G5
Р‘РѕС‚РёРЅРєРё	С€С‚.	11800	РћР±СѓРІСЊ РґР»СЏ РІР°СЃ	Rieker	Р–РµРЅСЃРєР°СЏ РѕР±СѓРІСЊ	15	11	Р‘РѕС‚РёРЅРєРё РЅР° РјРѕР»РЅРёРё СЃ РґРµРєРѕСЂР°С‚РёРІРЅРѕР№ РїСЂСЏР¶РєРѕР№ FRAU	NaN	1417	F427R5
РџРѕР»СѓР±РѕС‚РёРЅРєРё	С€С‚.	4600	Kari	CROSBY	Р–РµРЅСЃРєР°СЏ РѕР±СѓРІСЊ	3	13	РџРѕР»СѓР±РѕС‚РёРЅРєРё Р‘РѕС‚РёРЅРєРё С‡РµСЂРЅС‹Рµ Р·РёРјРЅРёРµ, РјРµС…	NaN	1418	N457T5
РўСѓС„Р»Рё	С€С‚.	12400	Kari	Kari	Р–РµРЅСЃРєР°СЏ РѕР±СѓРІСЊ	16	5	РўСѓС„Р»Рё Luiza Belly Р¶РµРЅСЃРєРёРµ Kate-lazo С‡РµСЂРЅС‹Рµ РёР· РЅР°С‚СѓСЂР°Р»СЊРЅРѕР№ Р·Р°РјС€Рё	NaN	1419	D364R4
РўР°РїРѕС‡РєРё	С€С‚.	9900	РћР±СѓРІСЊ РґР»СЏ РІР°СЃ	CROSBY	РњСѓР¶СЃРєР°СЏ РѕР±СѓРІСЊ	17	15	РњСѓР¶СЃРєРёРµ РєРѕР¶Р°РЅС‹Рµ С‚Р°РїРѕС‡РєРё "РџСЂРѕС„РёР»СЊ РЎ.Р”Р°Р»Рё"В 	NaN	1420	S326R5
РџРѕР»СѓР±РѕС‚РёРЅРєРё	С€С‚.	1700	Kari	Kari	Р–РµРЅСЃРєР°СЏ РѕР±СѓРІСЊ	2	7	РџРѕР»СѓР±РѕС‚РёРЅРєРё kari Р¶РµРЅСЃРєРёРµ WB2020SS-26, СЂР°Р·РјРµСЂ 38, С†РІРµС‚: С‡РµСЂРЅС‹Р№	NaN	1421	L754R4
РљСЂРѕСЃСЃРѕРІРєРё	С€С‚.	2800	РћР±СѓРІСЊ РґР»СЏ РІР°СЃ	Rieker	РњСѓР¶СЃРєР°СЏ РѕР±СѓРІСЊ	18	3	РљСЂРѕСЃСЃРѕРІРєРё РјСѓР¶СЃРєРёРµ TOFA	NaN	1422	M542T5
РўСѓС„Р»Рё	С€С‚.	4399	РћР±СѓРІСЊ РґР»СЏ РІР°СЃ	Rieker	Р–РµРЅСЃРєР°СЏ РѕР±СѓРІСЊ	3	12	РўСѓС„Р»Рё Rieker Р¶РµРЅСЃРєРёРµ РґРµРјРёСЃРµР·РѕРЅРЅС‹Рµ, СЂР°Р·РјРµСЂ 36, С†РІРµС‚ РєРѕСЂРёС‡РЅРµРІС‹Р№	NaN	1423	D268G5
РЎР°РїРѕРіРё	С€С‚.	4699	Kari	CROSBY	Р–РµРЅСЃРєР°СЏ РѕР±СѓРІСЊ	2	5	РЎР°РїРѕРіРё Р·Р°РјС€Р° Р¦РІРµС‚: СЃРёРЅРёР№	NaN	1424	T324F5
РўР°РїРѕС‡РєРё	С€С‚.	599	Kari	Rieker	РњСѓР¶СЃРєР°СЏ РѕР±СѓРІСЊ	20	2	РўР°РїРѕС‡РєРё РјСѓР¶СЃРєРёРµ СЃРёРЅ СЂ.41	NaN	1425	K358H6
Р‘РѕС‚РёРЅРєРё	С€С‚.	2300	РћР±СѓРІСЊ РґР»СЏ РІР°СЃ	Rieker	Р–РµРЅСЃРєР°СЏ РѕР±СѓРІСЊ	2	7	Р–РµРЅСЃРєРёРµ Р‘РѕС‚РёРЅРєРё РґРµРјРёСЃРµР·РѕРЅРЅС‹Рµ	NaN	1426	H535R5
\.


--
-- TOC entry 4931 (class 0 OID 25692)
-- Dependencies: 224
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, first_name, last_name, patronymic, login, password, status) FROM stdin;
641	Р’РµСЃРµРЅРёСЏ	РќРёРєРёС„РѕСЂРѕРІР°	РќРёРєРѕР»Р°РµРІРЅР°	94d5ous@gmail.com	uzWC67	РђРґРјРёРЅРёСЃС‚СЂР°С‚РѕСЂ
642	Р СѓСЃР»Р°РЅ	РЎР°Р·РѕРЅРѕРІ	Р“РµСЂРјР°РЅРѕРІРёС‡	uth4iz@mail.com	2L6KZG	РђРґРјРёРЅРёСЃС‚СЂР°С‚РѕСЂ
643	РЎРµСЂР°С„РёРј	РћРґРёРЅС†РѕРІ	РђСЂС‚С‘РјРѕРІРёС‡	yzls62@outlook.com	JlFRCZ	РђРґРјРёРЅРёСЃС‚СЂР°С‚РѕСЂ
644	РњРёС…Р°РёР»	РЎС‚РµРїР°РЅРѕРІ	РђСЂС‚С‘РјРѕРІРёС‡	1diph5e@tutanota.com	8ntwUp	РњРµРЅРµРґР¶РµСЂ
645	РџРµС‚СЂ	Р’РѕСЂСЃРёРЅ	Р•РІРіРµРЅСЊРµРІРёС‡	tjde7c@yahoo.com	YOyhfR	РњРµРЅРµРґР¶РµСЂ
646	Р•Р»РµРЅР°	РЎС‚Р°СЂРёРєРѕРІР°	РџР°РІР»РѕРІРЅР°	wpmrc3do@tutanota.com	RSbvHv	РњРµРЅРµРґР¶РµСЂ
647	РђРЅРЅР°	РњРёС…Р°Р№Р»СЋРє	Р’СЏС‡РµСЃР»Р°РІРѕРІРЅР°	5d4zbu@tutanota.com	rwVDh9	РђРІС‚РѕСЂРёР·РёСЂРѕРІР°РЅРЅС‹Р№ РєР»РёРµРЅС‚
648	Р•Р»РµРЅР°	РЎРёС‚РґРёРєРѕРІР°	РђРЅР°С‚РѕР»СЊРµРІРЅР°	ptec8ym@yahoo.com	LdNyos	РђРІС‚РѕСЂРёР·РёСЂРѕРІР°РЅРЅС‹Р№ РєР»РёРµРЅС‚
649	РџРµС‚СЂ	Р’РѕСЂСЃРёРЅ	Р•РІРіРµРЅСЊРµРІРёС‡	1qz4kw@mail.com	gynQMT	РђРІС‚РѕСЂРёР·РёСЂРѕРІР°РЅРЅС‹Р№ РєР»РёРµРЅС‚
650	Р•Р»РµРЅР°	РЎС‚Р°СЂРёРєРѕРІР°	РџР°РІР»РѕРІРЅР°	4np6se@mail.com	AtnDjr	РђРІС‚РѕСЂРёР·РёСЂРѕРІР°РЅРЅС‹Р№ РєР»РёРµРЅС‚
\.


--
-- TOC entry 4942 (class 0 OID 0)
-- Dependencies: 219
-- Name: orders_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.orders_id_seq', 101, true);


--
-- TOC entry 4943 (class 0 OID 0)
-- Dependencies: 221
-- Name: pick-up_points_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."pick-up_points_id_seq"', 972, true);


--
-- TOC entry 4944 (class 0 OID 0)
-- Dependencies: 223
-- Name: shoes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.shoes_id_seq', 1426, true);


--
-- TOC entry 4945 (class 0 OID 0)
-- Dependencies: 225
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 650, true);


--
-- TOC entry 4766 (class 2606 OID 25701)
-- Name: order_items order_items_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_items
    ADD CONSTRAINT order_items_pkey PRIMARY KEY (order_number, shoe_id);


--
-- TOC entry 4768 (class 2606 OID 25703)
-- Name: orders orders_pkye; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkye PRIMARY KEY (order_number);


--
-- TOC entry 4770 (class 2606 OID 25705)
-- Name: pick-up_points pick-up_points_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."pick-up_points"
    ADD CONSTRAINT "pick-up_points_pkey" PRIMARY KEY (id);


--
-- TOC entry 4772 (class 2606 OID 25707)
-- Name: shoes shoes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shoes
    ADD CONSTRAINT shoes_pkey PRIMARY KEY (id);


--
-- TOC entry 4774 (class 2606 OID 25709)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- TOC entry 4775 (class 2606 OID 25710)
-- Name: order_items order_items_orders_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_items
    ADD CONSTRAINT order_items_orders_fkey FOREIGN KEY (order_number) REFERENCES public.orders(order_number) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 4776 (class 2606 OID 25715)
-- Name: order_items order_items_shoes_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_items
    ADD CONSTRAINT order_items_shoes_fkey FOREIGN KEY (shoe_id) REFERENCES public.shoes(id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- TOC entry 4777 (class 2606 OID 25720)
-- Name: orders orders_pickup_point_code; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pickup_point_code FOREIGN KEY (pickup_point_code) REFERENCES public."pick-up_points"(id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- TOC entry 4778 (class 2606 OID 25725)
-- Name: orders orders_users_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_users_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


-- Completed on 2026-11-13 13:29:40

--
-- PostgreSQL database dump complete
--


