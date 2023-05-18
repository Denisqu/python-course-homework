CREATE TABLE "case_domain" (
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR(100) NOT NULL
);

CREATE TABLE "case_type" (
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR(100) NOT NULL
);

CREATE TABLE "client" (
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR(100) NOT NULL
);

CREATE TABLE "lawyer" (
  "id" SERIAL PRIMARY KEY,
  "price_multiplier" DECIMAL(12, 2) NOT NULL,
  "name" VARCHAR(100) NOT NULL
);

CREATE TABLE "service_type" (
  "id" SERIAL PRIMARY KEY,
  "base_price" DECIMAL(12, 2) NOT NULL,
  "name" VARCHAR(100) NOT NULL
);

CREATE TABLE "case" (
  "id" SERIAL PRIMARY KEY,
  "description" VARCHAR(2000) NOT NULL,
  "id_lawyer" INTEGER NOT NULL,
  "id_client" INTEGER NOT NULL,
  "id_case_type" INTEGER NOT NULL,
  "id_case_domain" INTEGER NOT NULL,
  "status" BOOLEAN NOT NULL,
  "id_service_type" INTEGER NOT NULL
);

CREATE INDEX "idx_case__id_case_domain" ON "case" ("id_case_domain");

CREATE INDEX "idx_case__id_case_type" ON "case" ("id_case_type");

CREATE INDEX "idx_case__id_client" ON "case" ("id_client");

CREATE INDEX "idx_case__id_lawyer" ON "case" ("id_lawyer");

CREATE INDEX "idx_case__id_service_type" ON "case" ("id_service_type");

ALTER TABLE "case" ADD CONSTRAINT "fk_case__id_case_domain" FOREIGN KEY ("id_case_domain") REFERENCES "case_domain" ("id") ON DELETE CASCADE;

ALTER TABLE "case" ADD CONSTRAINT "fk_case__id_case_type" FOREIGN KEY ("id_case_type") REFERENCES "case_type" ("id") ON DELETE CASCADE;

ALTER TABLE "case" ADD CONSTRAINT "fk_case__id_client" FOREIGN KEY ("id_client") REFERENCES "client" ("id") ON DELETE CASCADE;

ALTER TABLE "case" ADD CONSTRAINT "fk_case__id_lawyer" FOREIGN KEY ("id_lawyer") REFERENCES "lawyer" ("id") ON DELETE CASCADE;

ALTER TABLE "case" ADD CONSTRAINT "fk_case__id_service_type" FOREIGN KEY ("id_service_type") REFERENCES "service_type" ("id") ON DELETE CASCADE;

CREATE TABLE "lawyer_service_type" (
  "id_service_type" INTEGER NOT NULL,
  "id_lawyer" INTEGER NOT NULL,
  PRIMARY KEY ("id_service_type", "id_lawyer")
);

CREATE INDEX "idx_lawyer_service_type__id_lawyer" ON "lawyer_service_type" ("id_lawyer");

ALTER TABLE "lawyer_service_type" ADD CONSTRAINT "fk_lawyer_service_type__id_lawyer" FOREIGN KEY ("id_lawyer") REFERENCES "lawyer" ("id") ON DELETE CASCADE;

ALTER TABLE "lawyer_service_type" ADD CONSTRAINT "fk_lawyer_service_type__id_service_type" FOREIGN KEY ("id_service_type") REFERENCES "service_type" ("id") ON DELETE CASCADE