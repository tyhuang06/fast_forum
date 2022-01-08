-- upgrade --
ALTER TABLE "users" ADD "profile_pic" VARCHAR(200) NOT NULL  DEFAULT 'default.jpg';
-- downgrade --
ALTER TABLE "users" DROP COLUMN "profile_pic";
