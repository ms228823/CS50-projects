select people.name from people
inner join stars on people.id = stars.person_id
inner join movies on stars.movie_id = movies.id
where movies.title = 'Toy Story';
