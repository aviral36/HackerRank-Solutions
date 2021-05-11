SELECT  
CASE 
WHEN A+B<=C OR A+C<=B OR B+C<=A THEN 'Not A Triangle'
ELSE 
    CASE
        WHEN A=B AND A=C THEN 'Equilateral'
        WHEN (A=B AND A<>C) OR (A=C AND A<>B) OR (B=C AND A<>C) THEN 'Isosceles'
        WHEN A<>B AND B<>C AND C<>A THEN 'Scalene'
    END
END
FROM TRIANGLES;
