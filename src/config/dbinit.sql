-- Users Table
CREATE TABLE Users (
    user_id STRING PRIMARY KEY,
    username STRING NOT NULL,
    join_date INT NOT NULL,
    last_used_date INT
);

-- Videos Table
CREATE TABLE Videos (
    video_id STRING PRIMARY KEY,
    title STRING NOT NULL,
    url STRING NOT NULL,
    user_id STRING REFERENCES Users(user_id),
    create_date INT NOT NULL
);

-- BestOfs Table
CREATE TABLE BestOfs (
    bestof_id STRING PRIMARY KEY,
    title STRING NOT NULL,
    duration INT NOT NULL,
    video_id STRING REFERENCES Videos(video_id),
    create_date INT NOT NULL,
    XML_FCPX TEXT
);