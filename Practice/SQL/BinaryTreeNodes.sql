/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT N,
CASE 
WHEN P IS NULL THEN "Root" 
ELSE
CASE WHEN N NOT IN (SELECT DISTINCT P FROM BST WHERE P IS NOT NULL) THEN "Leaf"
ELSE "Inner"
    END
END
FROM BST
ORDER BY N;

--SELECT N FROM BST WHERE N NOT IN (SELECT DISTINCT P FROM BST WHERE P IS NOT NULL);
