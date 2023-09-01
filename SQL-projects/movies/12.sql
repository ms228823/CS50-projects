select movies.title from people
inner join stars on people.id = stars.person_id
inner join movies on stars.movie_id = movies.id
where people.name = 'Johnny Depp'
and movies.title
in
(select movies.title from people
inner join stars on people.id = stars.person_id
inner join movies on stars.movie_id = movies.id
where people.name = 'Helena Bonham Carter');