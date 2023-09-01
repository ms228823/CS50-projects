select people.name from people
inner join directors on people.id = directors.person_id
inner join movies on directors.movie_id = movies.id
inner join ratings on ratings.movie_id = movies.id
where ratings.rating >= 9;