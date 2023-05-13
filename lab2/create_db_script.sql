
Editing diagram Denis1902/test

Explore
Denis1902
Log out
CREATE TABLE "category" (
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR(100) NOT NULL
);

CREATE TABLE "group" (
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR(255) NOT NULL
);

CREATE TABLE "student" (
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR(128) NOT NULL,
  "id_group" INTEGER NOT NULL,
  "git" VARCHAR(300) NOT NULL
);

CREATE INDEX "idx_student__id_group" ON "student" ("id_group");

ALTER TABLE "student" ADD CONSTRAINT "fk_student__id_group" FOREIGN KEY ("id_group") REFERENCES "group" ("id") ON DELETE CASCADE;

CREATE TABLE "task_difficulty" (
  "id" SERIAL PRIMARY KEY,
  "name" TEXT NOT NULL
);

CREATE TABLE "task" (
  "id" SERIAL PRIMARY KEY,
  "id_category" INTEGER NOT NULL,
  "name" VARCHAR(255) NOT NULL,
  "description" TEXT,
  "code" TEXT NOT NULL,
  "id_task_difficulty" INTEGER NOT NULL
);

CREATE INDEX "idx_task__id_category" ON "task" ("id_category");

CREATE INDEX "idx_task__id_task_difficulty" ON "task" ("id_task_difficulty");

ALTER TABLE "task" ADD CONSTRAINT "fk_task__id_category" FOREIGN KEY ("id_category") REFERENCES "category" ("id") ON DELETE CASCADE;

ALTER TABLE "task" ADD CONSTRAINT "fk_task__id_task_difficulty" FOREIGN KEY ("id_task_difficulty") REFERENCES "task_difficulty" ("id") ON DELETE CASCADE;

CREATE TABLE "task_student" (
  "id_student" INTEGER NOT NULL,
  "id_task" INTEGER NOT NULL,
  "status" BOOLEAN NOT NULL,
  PRIMARY KEY ("id_student", "id_task")
);

CREATE INDEX "idx_task_student__id_task" ON "task_student" ("id_task");

ALTER TABLE "task_student" ADD CONSTRAINT "fk_task_student__id_student" FOREIGN KEY ("id_student") REFERENCES "student" ("id") ON DELETE CASCADE;

ALTER TABLE "task_student" ADD CONSTRAINT "fk_task_student__id_task" FOREIGN KEY ("id_task") REFERENCES "task" ("id") ON DELETE CASCADE;

CREATE TABLE "teacher" (
  "id" SERIAL PRIMARY KEY,
  "name" TEXT NOT NULL
);

CREATE TABLE "teacher_groups" (
  "id_teacher" INTEGER NOT NULL,
  "id_group" INTEGER NOT NULL,
  PRIMARY KEY ("id_teacher", "id_group")
);

CREATE INDEX "idx_teacher_groups__id_group" ON "teacher_groups" ("id_group");

ALTER TABLE "teacher_groups" ADD CONSTRAINT "fk_teacher_groups__id_group" FOREIGN KEY ("id_group") REFERENCES "group" ("id") ON DELETE CASCADE;

ALTER TABLE "teacher_groups" ADD CONSTRAINT "fk_teacher_groups__id_teacher" FOREIGN KEY ("id_teacher") REFERENCES "teacher" ("id") ON DELETE CASCADE