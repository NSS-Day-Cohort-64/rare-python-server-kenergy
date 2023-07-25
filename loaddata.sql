CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);

CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`category_id`) REFERENCES `Categories` (`id`)
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

INSERT INTO "Users" VALUES (null, "Lance", "Buckley", "lance@gmail.com", "Painter in the streets but a developer in the sheets", "Lancelot", "123abc", "https://ca.slack-edge.com/T03F2SDTJ-U04U46Q3CQZ-f1b4f383d0a2-512", "March 12th, 2021", True);
INSERT INTO "Users" VALUES (null, "Belle", "Hollander", "belle@gmail.com", "Future TA", "TeacherAssistantBelle", "TA", "https://ca.slack-edge.com/T03F2SDTJ-U04KAQ5RU1H-10b66acf02a3-72", "December 25th, 2022", True);
INSERT INTO "Users" VALUES (null, "Jonathan", "VanDuyne", "jonathan@gmail.com", "Ask me about my stocks", "Mr.MoneyBags", "$$$$", "https://ca.slack-edge.com/T03F2SDTJ-U04RA3YKLCW-5724d71c11af-72", "July 4th, 2023", True);
INSERT INTO "Users" VALUES (null, "Sam", "Thrasher", "sam@gmail.com", "Ask me about barbie", "Kenergy", "password", "https://i.imgur.com/AuZYuAL.jpg", "January 16th, 1996", True);
INSERT INTO "Users" VALUES (null, "Steve", "Brownlee", "steve@gmail.com", "And why do we think that is gang?", "Coach", "goldenrod", "https://i.imgur.com/Ho5gBlC.jpg", "June 21st, 1948", True);

INSERT INTO "Subscriptions" VALUES (null, 1, 2, "July 25th, 2023");
INSERT INTO "Subscriptions" VALUES (null, 3, 2, "July 26th, 2023");
INSERT INTO "Subscriptions" VALUES (null, 4, 3, "July 27th, 2023");
INSERT INTO "Subscriptions" VALUES (null, 5, 4, "July 28th, 2023");
INSERT INTO "Subscriptions" VALUES (null, 2, 5, "July 29th, 2023");
INSERT INTO "Subscriptions" VALUES (null, 1, 3, "July 30th, 2023");
INSERT INTO "Subscriptions" VALUES (null, 5, 1, "July 31st, 2023");
INSERT INTO "Subscriptions" VALUES (null, 3, 4, "August 1st, 2023");
INSERT INTO "Subscriptions" VALUES (null, 1, 5, "August 2nd, 2023");
INSERT INTO "Subscriptions" VALUES (null, 4, 2, "August 3rd, 2023");

INSERT INTO "Posts" VALUES (null, 1, 2, "The History of Board Games I like", "July 25th, 2023", "https://static.wikia.nocookie.net/lancer/images/2/2f/LANCER.jpg/revision/latest?cb=20200509101840", "Absolutely loving Lancer right now! 🎮 The deep and immersive gameplay, along with the captivating sci-fi universe, keeps me hooked for hours. Whether piloting mechs or exploring alien worlds, it's an epic adventure that never disappoints! #Gaming #LancerLove", True);
INSERT INTO "Posts" VALUES (null, 3, 4, "Navigating the Economic Landscape", "August 5th, 2023", "https://g.foolcdn.com/editorial/images/721776/growth-stock-chart.jpg", "As an avid economist, I find the dynamics of the global economy endlessly fascinating. The intricate interplay of market forces, trade policies, and technological advancements shapes our financial world. Sharing my insights and predictions on the current economic trends. #Economy #Finance #Insights", True);
INSERT INTO "Posts" VALUES (null, 2, 5, "The Magic of Barbie: A Timeless Classic", "August 10th, 2023", "https://hips.hearstapps.com/hmg-prod/images/rev-1-barbie-tp-0002-high-res-jpeg-647e152f50df6.jpeg?crop=0.8477702191987906xw:1xh;center,top", "Just watched the movie Barbie, and I must say it's an absolute delight! ✨ The enchanting storyline, stunning animation, and inspiring messages make it a timeless classic for all ages. Kudos to the creators for bringing such joy and positivity to the screen! #BarbieMovie #Animation #FamilyFavorite", True);
INSERT INTO "Posts" VALUES (null, 4, 3, "Remembering Jimmy Carter: A Remarkable Leader", "August 15th, 2023", "https://media.vanityfair.com/photos/63fe697df4d781753ce36e1d/master/w_2560%2Cc_limit/vf223-carter-hwood-south-sitestory.png", "Reflecting on the legacy of Jimmy Carter, both as a person and a president, is truly inspiring. 🇺🇸 His unwavering dedication to peace, human rights, and humanitarian efforts left a profound impact on the world. We can learn so much from his leadership and commitment to making the world a better place. #JimmyCarter #Leadership #Inspiration", True);

INSERT INTO "Comments" VALUES (null, 4, 5, "A touching tribute to a man who isn't dead");
INSERT INTO "Comments" VALUES (null, 1, 4, "Wow this looks so fun Lance!");
INSERT INTO "Comments" VALUES (null, 1, 2, "Wow this looks so boring Lance!");
INSERT INTO "Comments" VALUES (null, 3, 1, "That's my junior dev!");
INSERT INTO "Comments" VALUES (null, 3, 3, "I cry everytime Ken takes his shirt off. Real touching stuff");

INSERT INTO "Reactions" VALUES (null, "happy", "https://w7.pngwing.com/pngs/7/748/png-transparent-facebook-like-button-chemical-reaction-computer-icons-facebook-blue-text-hand.png");
INSERT INTO "Reactions" VALUES (null, "love", "https://e7.pngegg.com/pngimages/540/262/png-clipart-white-heart-social-media-facebook-like-button-heart-emoticon-facebook-live-love-miscellaneous-text.png");
INSERT INTO "Reactions" VALUES (null, "shock", "https://www.vhv.rs/dpng/d/487-4877648_transparent-fb-reactions-png-facebook-wow-emoji-png.png");
INSERT INTO "Reactions" VALUES (null, "mad", "https://p1.hiclipart.com/preview/147/39/662/56-facebook-emoji-angry-emoticon-illustration-png-clipart.jpg");
INSERT INTO "Reactions" VALUES (null, "sad", "https://www.clipartmax.com/png/middle/186-1862456_sad-emo-emoticon-face-icon-facebook-emoji-sad-png.png");
INSERT INTO "Reactions" VALUES (null, "rootin tootin", "https://i.imgur.com/EsAgsm6.png");

INSERT INTO "PostReactions" VALUES (null, 2, 4, 1);
INSERT INTO "PostReactions" VALUES (null, 5, 1, 1);
INSERT INTO "PostReactions" VALUES (null, 1, 2, 1);
INSERT INTO "PostReactions" VALUES (null, 3, 3, 1);
INSERT INTO "PostReactions" VALUES (null, 3, 3, 2);
INSERT INTO "PostReactions" VALUES (null, 4, 4, 1);
INSERT INTO "PostReactions" VALUES (null, 2, 5, 1);
INSERT INTO "PostReactions" VALUES (null, 4, 2, 2);
INSERT INTO "PostReactions" VALUES (null, 2, 3, 2);
INSERT INTO "PostReactions" VALUES (null, 1, 1, 3);
INSERT INTO "PostReactions" VALUES (null, 3, 5, 3);
INSERT INTO "PostReactions" VALUES (null, 5, 6, 3);
INSERT INTO "PostReactions" VALUES (null, 1, 1, 4);
INSERT INTO "PostReactions" VALUES (null, 2, 2, 4);
INSERT INTO "PostReactions" VALUES (null, 3, 3, 4);
INSERT INTO "PostReactions" VALUES (null, 4, 5, 4);

INSERT INTO "Tags" VALUES (null, "Javascript");
INSERT INTO "Tags" VALUES (null, "Python");
INSERT INTO "Tags" VALUES (null, "SQL");
INSERT INTO "Tags" VALUES (null, "React");
INSERT INTO "Tags" VALUES (null, "Django");
INSERT INTO "Tags" VALUES (null, "Lancer");
INSERT INTO "Tags" VALUES (null, "Dungeons and Dragons");
INSERT INTO "Tags" VALUES (null, "Pathfinder");
INSERT INTO "Tags" VALUES (null, "Barbie Doll");
INSERT INTO "Tags" VALUES (null, "Ken Doll");
INSERT INTO "Tags" VALUES (null, "Allen Doll");
INSERT INTO "Tags" VALUES (null, "Stocks");
INSERT INTO "Tags" VALUES (null, "Bonds");
INSERT INTO "Tags" VALUES (null, "Dollars");
INSERT INTO "Tags" VALUES (null, "Jimmy Carter");
INSERT INTO "Tags" VALUES (null, "Barrack Obama");
INSERT INTO "Tags" VALUES (null, "John F. Kennedy");

INSERT INTO "PostTags" VALUES (null, 1, 6);
INSERT INTO "PostTags" VALUES (null, 2, 12);
INSERT INTO "PostTags" VALUES (null, 3, 9);
INSERT INTO "PostTags" VALUES (null, 4, 15);

INSERT INTO "Categories" VALUES (null, "News");
INSERT INTO "Categories" VALUES (null, "Sports");
INSERT INTO "Categories" VALUES (null, "Politics");
INSERT INTO "Categories" VALUES (null, "Entertainment");
INSERT INTO "Categories" VALUES (null, "Finance");
INSERT INTO "Categories" VALUES (null, "Current Events");


