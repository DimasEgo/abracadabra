-- 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT s.student,
round(avg(g.grade), 2) AS avg_grade
FROM grades g
LEFT JOIN students s ON s.id = g.student
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 5

-- 1 студент із найвищим середнім балом з одного предмета
SELECT d.discipline, s.student, round(avg(g.grade),2) AS grade
from grades g
LEFT JOIN students s on s.id = g.student
LEFT JOIN disciplines d ON d.id =g.discipline
WHERE  d.id = 1
GROUP BY s.id , d.id
ORder by (round(avg(g.grade), 2)) DESC
LIMIT 1

-- Середній бал в групі по одному предмету.
SELECT d.discipline, gr.[group], round(avg(g.grade),2) AS grade
from grades g
LEFT JOIN students s on s.id = g.student
LEFT JOIN disciplines d ON d.id =g.discipline
LEFT JOIN [groups] gr ON gr.id =s.[group]
WHERE  d.id = 2
GROUP BY gr.id
ORder by grade DESC
LIMIT 1

-- Середній бал у потоці.
SELECT round(avg(grade), 2) as avg_grade
FROM grades

-- Які курси читає викладач.
SELECT DISTINCT d.discipline, t.teacher
FROM teachers t
LEFT JOIN disciplines d ON d.teacher = t.id
WHERE d.teacher = 2;

-- Список студентів у групі.
SELECT DISTINCT s.student, s."group"
FROM students s
WHERE s."group" =1

-- Оцінки студентів у групі з предмета.
SELECT d.discipline, gr.[group], s.student, g.date_of, g.grade
FROM grades g
LEFT JOIN students s ON s.id = g.student
LEFT JOIN disciplines d ON d.id = g.discipline
LEFT JOIN [groups] gr  ON gr.id = s.[group]
WHERE d.id = 2 and gr.id=1

-- Оцінки студентів у групі з предмета на останньому занятті.
SELECT d.discipline, gr.[group], s.student, g.date_of, g.grade
FROM grades g
LEFT JOIN students s ON s.id = g.student
LEFT JOIN disciplines d ON d.id = g.discipline
LEFT JOIN [groups] gr  ON gr.id = s.[group]
WHERE d.id = 1 and gr.id=3 and g.date_of = (
SELECT g.date_of
FROM grades g
LEFT JOIN students s on s.id =g.student
LEFT JOIN [groups] gr on gr.id =s.[group]
WHERE g.discipline =1
and gr.id =3
ORDER by g.date_of  DESC
limit 1
)
order by date_of DESC

-- Список курсів, які відвідує студент.
SELECT DISTINCT s.student, d.discipline
FROM grades g
LEFT JOIN students s ON s.id = g.student
LEFT JOIN disciplines d ON d.id = g.discipline
WHERE g.student =7

-- Список курсів, які студенту читає викладач.
SELECT distinct s.student, t.teacher, d.discipline
from grades g
LEFT JOIN students s on s.id = g.student
LEFT JOIN disciplines d  on d.id = g.discipline
LEFT JOIN teachers t  on t.id = d.teacher
WHERE g.student =12 and t.id =2

-- Середній бал, який викладач ставить студенту.
SELECT DISTINCT s.student, t.teacher, round(avg(grade), 2) as avg_grade
from grades g
LEFT JOIN students s on s.id = g.student
LEFT JOIN disciplines d  on d.id = g.discipline
LEFT JOIN teachers t  on t.id = d.teacher
WHERE g.student = 13 and t.id =2
GROUP BY s.student, t.teacher

-- Середній бал, який ставить викладач.
SELECT DISTINCT t.teacher, round(avg(grade), 2) as avg_grade
from grades g
LEFT JOIN disciplines d  on d.id = g.discipline
LEFT JOIN teachers t  on t.id = d.teacher
WHERE t.id =2
GROUP BY t.teacher