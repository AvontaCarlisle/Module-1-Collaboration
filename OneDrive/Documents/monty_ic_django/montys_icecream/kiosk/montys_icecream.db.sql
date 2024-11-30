BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "flavors" (
	"id"	INTEGER UNIQUE,
	"flavor"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ice_cream_type" (
	"id"	INTEGER UNIQUE,
	"type"	TEXT,
	"price"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "toppings" (
	"id"	INTEGER UNIQUE,
	"name"	TEXT,
	"price"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "flavors" VALUES (0,'');
INSERT INTO "flavors" VALUES (1,'vanilla');
INSERT INTO "flavors" VALUES (3,'cookies & cream');
INSERT INTO "flavors" VALUES (4,'strawberry');
INSERT INTO "flavors" VALUES (5,'butter pecan');
INSERT INTO "flavors" VALUES (6,'birthday cake');
INSERT INTO "flavors" VALUES (7,'banana split');
INSERT INTO "flavors" VALUES (8,'almond joy');
INSERT INTO "flavors" VALUES (9,'maple walnut');
INSERT INTO "flavors" VALUES (10,'cookie dough');
INSERT INTO "flavors" VALUES (11,'mango');
INSERT INTO "flavors" VALUES (12,'vanilla & py');
INSERT INTO "flavors" VALUES (13,'apple py');
INSERT INTO "ice_cream_type" VALUES (1,'cone',1);
INSERT INTO "ice_cream_type" VALUES (2,'milkshake',3);
INSERT INTO "ice_cream_type" VALUES (3,'cake',5);
INSERT INTO "ice_cream_type" VALUES (4,'yogurt',2);
INSERT INTO "toppings" VALUES (1,'sprinkles',0.25);
INSERT INTO "toppings" VALUES (2,'frosting',0.25);
INSERT INTO "toppings" VALUES (3,'nuts',0.25);
INSERT INTO "toppings" VALUES (4,'fruit',0.25);
INSERT INTO "toppings" VALUES (5,'cookie crumble',0.25);
INSERT INTO "toppings" VALUES (6,'marshmallows',0.25);
INSERT INTO "toppings" VALUES (7,'monty sauce',0.3);
COMMIT;