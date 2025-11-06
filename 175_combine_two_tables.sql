-- LeetCode 175: Combine Two Tables
-- Problem: Report the first name, last name, city, and state of each person.
-- If the address of a personId is not present in the Address table, report null instead.

SELECT 
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a ON p.personId = a.personId;

