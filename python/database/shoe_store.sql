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


ALTER TABLE public.order_items OWNER TO postgres;

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


ALTER TABLE public.orders OWNER TO postgres;

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


ALTER SEQUENCE public.orders_id_seq OWNER TO postgres;

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


ALTER TABLE public."pick-up_points" OWNER TO postgres;

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


ALTER SEQUENCE public."pick-up_points_id_seq" OWNER TO postgres;

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


ALTER TABLE public.shoes OWNER TO postgres;

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


ALTER SEQUENCE public.shoes_id_seq OWNER TO postgres;

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


ALTER TABLE public.users OWNER TO postgres;

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


ALTER SEQUENCE public.users_id_seq OWNER TO postgres;

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
2025-02-27	2025-04-20	644	901	Завершен	1	92
2022-09-28	2025-04-21	641	902	Завершен	11	93
2025-03-21	2025-04-22	642	903	Завершен	2	94
2025-02-20	2025-04-23	643	904	Завершен	11	95
2025-03-17	2025-04-24	644	905	Завершен	2	96
2025-03-01	2025-04-25	641	906	Завершен	15	97
\N	2025-04-26	642	907	Завершен	3	98
2025-03-31	2025-04-27	643	908	Новый 	19	99
2025-04-02	2025-04-28	644	909	Новый 	5	100
2025-04-03	2025-04-29	644	910	Новый 	19	101
\.


--
-- TOC entry 4927 (class 0 OID 25682)
-- Dependencies: 220
-- Data for Name: pick-up_points; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."pick-up_points" (town, street, id, postal_code, house) FROM stdin;
г. Лесной	ул. Вишневая	1	420151	32
г. Лесной	ул. Подгорная	2	125061	8
г. Лесной	ул. Шоссейная	3	630370	24
г. Лесной	ул. Зеленая	4	400562	32
г. Лесной	ул. Маяковского	5	614510	47
г. Лесной	ул. Светлая	6	410542	46
г. Лесной	ул. Цветочная	7	620839	8
г. Лесной	ул. Коммунистическая	8	443890	1
г. Лесной	ул. Спортивная	9	603379	46
г. Лесной	ул. Гоголя	10	603721	41
г. Лесной	ул. Северная	11	410172	13
г. Лесной	ул. Молодежная	12	614611	50
г.Лесной	ул. Новая	13	454311	19
г.Лесной	ул. Октябрьская	14	660007	19
г. Лесной	ул. Садовая	15	603036	4
г.Лесной	ул. Фрунзе	16	394060	43
г. Лесной	ул. Школьная	17	410661	50
г. Лесной	ул. Коммунистическая	18	625590	20
г. Лесной	ул. 8 Марта	19	625683	NaN
г.Лесной	ул. Комсомольская	20	450983	26
г. Лесной	ул. Чехова	21	394782	3
г. Лесной	ул. Дзержинского	22	603002	28
г. Лесной	ул. Набережная	23	450558	30
г. Лесной	ул. Чехова	24	344288	1
г.Лесной	ул. Степная	25	614164	30
г. Лесной	ул. Коммунистическая	26	394242	43
г. Лесной	ул. Солнечная	27	660540	25
г. Лесной	ул. Шоссейная	28	125837	40
г. Лесной	ул. Партизанская	29	125703	49
г. Лесной	ул. Победы	30	625283	46
г. Лесной	ул. Полевая	31	614753	35
г. Лесной	ул. Маяковского	32	426030	44
г. Лесной ул. Клубная	44	33	450375	NaN
г. Лесной	ул. Некрасова	34	625560	12
г. Лесной	ул. Комсомольская	35	630201	17
г. Лесной	ул. Мичурина	36	190949	26
\.


--
-- TOC entry 4929 (class 0 OID 25686)
-- Dependencies: 222
-- Data for Name: shoes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.shoes (name, unit, price, supplier, manufacturer, category, discount, quantity_in_stock, description, image, id, article) FROM stdin;
Ботинки	шт.	4990	Kari	Kari	Женская обувь	3	6	Женские Ботинки демисезонные kari	1.jpg	1397	А112Т4
Ботинки	шт.	3244	Обувь для вас	Marco Tozzi	Женская обувь	2	13	Ботинки Marco Tozzi женские демисезонные, размер 39, цвет бежевый	2.jpg	1398	F635R4
Туфли	шт.	4499	Kari	Kari	Мужская обувь	4	5	Туфли kari мужские классика MYZ21AW-450A, размер 43, цвет: черный	3.jpg	1399	H782T5
Ботинки	шт.	5900	Kari	Рос	Мужская обувь	2	8	Мужские ботинки Рос-Обувь кожаные с натуральным мехом	4.jpg	1400	G783F5
Ботинки	шт.	3800	Обувь для вас	Rieker	Мужская обувь	2	16	B3430/14 Полуботинки мужские Rieker	5.jpg	1401	J384T6
Кроссовки	шт.	4100	Обувь для вас	Рос	Мужская обувь	3	6	129615-4 Кроссовки мужские	6.jpg	1402	D572U8
Туфли	шт.	2700	Kari	Marco Tozzi	Женская обувь	2	14	Туфли Marco Tozzi женские летние, размер 39, цвет черный	7.jpg	1403	F572H7
Полуботинки	шт.	1890	Обувь для вас	Alessio Nesca	Женская обувь	4	4	Полуботинки Alessio Nesca женские 3-30797-47, размер 37, цвет: бордовый	8.jpg	1404	D329H3
Туфли	шт.	4300	Kari	Rieker	Женская обувь	2	6	Туфли Rieker женские демисезонные, размер 41, цвет коричневый	9.jpg	1405	B320R5
Туфли	шт.	2800	Kari	Kari	Женская обувь	3	15	Туфли kari женские TR-YR-413017, размер 37, цвет: черный	10.jpg	1406	G432E4
Полуботинки	шт.	2156	Обувь для вас	CROSBY	Мужская обувь	3	6	407700/01-01 Полуботинки мужские CROSBY	NaN	1407	S213E3
Полуботинки	шт.	1800	Kari	Kari	Женская обувь	2	14	Полуботинки kari женские MYZ20S-149, размер 41, цвет: черный	NaN	1408	E482R4
Кеды	шт.	5500	Обувь для вас	CROSBY	Мужская обувь	3	0	Кеды Caprice мужские демисезонные, размер 42, цвет черный	NaN	1409	S634B5
Полуботинки	шт.	2100	Обувь для вас	CROSBY	Мужская обувь	2	3	407700/01-02 Полуботинки мужские CROSBY	NaN	1410	K345R4
Туфли	шт.	5400	Обувь для вас	Rieker	Женская обувь	4	18	Туфли женские демисезонные Rieker артикул 55073-68/37	NaN	1411	O754F4
Ботинки	шт.	6600	Kari	Kari	Женская обувь	12	9	Ботинки женские зимние ROMER арт. 893167-01 Черный	NaN	1412	G531F4
Тапочки	шт.	500	Kari	Kari	Мужская обувь	13	0	Тапочки мужские Арт.70701-55-67син р.41	NaN	1413	J542F5
Ботинки	шт.	2700	Обувь для вас	Rieker	Мужская обувь	2	5	Мужские кожаные ботинки/мужские ботинки	NaN	1414	B431R5
Туфли	шт.	6800	Kari	CROSBY	Женская обувь	15	15	Туфли женские, ARGO, размер 38	NaN	1415	P764G4
Ботинки	шт.	10200	Kari	Alessio Nesca	Женская обувь	15	9	Ботинки женские, ARGO, размер 40	NaN	1416	C436G5
Ботинки	шт.	11800	Обувь для вас	Rieker	Женская обувь	15	11	Ботинки на молнии с декоративной пряжкой FRAU	NaN	1417	F427R5
Полуботинки	шт.	4600	Kari	CROSBY	Женская обувь	3	13	Полуботинки Ботинки черные зимние, мех	NaN	1418	N457T5
Туфли	шт.	12400	Kari	Kari	Женская обувь	16	5	Туфли Luiza Belly женские Kate-lazo черные из натуральной замши	NaN	1419	D364R4
Тапочки	шт.	9900	Обувь для вас	CROSBY	Мужская обувь	17	15	Мужские кожаные тапочки "Профиль С.Дали" 	NaN	1420	S326R5
Полуботинки	шт.	1700	Kari	Kari	Женская обувь	2	7	Полуботинки kari женские WB2020SS-26, размер 38, цвет: черный	NaN	1421	L754R4
Кроссовки	шт.	2800	Обувь для вас	Rieker	Мужская обувь	18	3	Кроссовки мужские TOFA	NaN	1422	M542T5
Туфли	шт.	4399	Обувь для вас	Rieker	Женская обувь	3	12	Туфли Rieker женские демисезонные, размер 36, цвет коричневый	NaN	1423	D268G5
Сапоги	шт.	4699	Kari	CROSBY	Женская обувь	2	5	Сапоги замша Цвет: синий	NaN	1424	T324F5
Тапочки	шт.	599	Kari	Rieker	Мужская обувь	20	2	Тапочки мужские син р.41	NaN	1425	K358H6
Ботинки	шт.	2300	Обувь для вас	Rieker	Женская обувь	2	7	Женские Ботинки демисезонные	NaN	1426	H535R5
\.


--
-- TOC entry 4931 (class 0 OID 25692)
-- Dependencies: 224
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, first_name, last_name, patronymic, login, password, status) FROM stdin;
641	Весения	Никифорова	Николаевна	94d5ous@gmail.com	uzWC67	Администратор
642	Руслан	Сазонов	Германович	uth4iz@mail.com	2L6KZG	Администратор
643	Серафим	Одинцов	Артёмович	yzls62@outlook.com	JlFRCZ	Администратор
644	Михаил	Степанов	Артёмович	1diph5e@tutanota.com	8ntwUp	Менеджер
645	Петр	Ворсин	Евгеньевич	tjde7c@yahoo.com	YOyhfR	Менеджер
646	Елена	Старикова	Павловна	wpmrc3do@tutanota.com	RSbvHv	Менеджер
647	Анна	Михайлюк	Вячеславовна	5d4zbu@tutanota.com	rwVDh9	Авторизированный клиент
648	Елена	Ситдикова	Анатольевна	ptec8ym@yahoo.com	LdNyos	Авторизированный клиент
649	Петр	Ворсин	Евгеньевич	1qz4kw@mail.com	gynQMT	Авторизированный клиент
650	Елена	Старикова	Павловна	4np6se@mail.com	AtnDjr	Авторизированный клиент
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

