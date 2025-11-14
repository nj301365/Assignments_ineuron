SELECT student.rollno, student.name, courses.cname 
FROM student
JOIN courses ON student.cid = courses.cid
WHERE courses.cname = 'Python';
