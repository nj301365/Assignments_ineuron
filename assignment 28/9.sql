-- Insert data into Courses table
INSERT INTO courses (cid, cname)
VALUES 
(1, 'Python'),
(2, 'Java'),
(3, 'C++');

-- Insert data into Student table
INSERT INTO student (rollno, name, cid)
VALUES 
(1, 'Alice', 1),  -- Alice is taking Python
(2, 'Bob', 2),    -- Bob is taking Java
(3, 'Charlie', 3), -- Charlie is taking C++
(4, 'David', 1);   -- David is taking Python
