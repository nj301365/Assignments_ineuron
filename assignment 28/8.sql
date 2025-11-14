-- Create Courses table
CREATE TABLE courses (
    cid INT PRIMARY KEY,
    cname VARCHAR(100)
);

-- Create Student table with foreign key reference to Courses
CREATE TABLE student (
    rollno INT PRIMARY KEY,
    name VARCHAR(100),
    cid INT,
    FOREIGN KEY (cid) REFERENCES courses(cid)
);
