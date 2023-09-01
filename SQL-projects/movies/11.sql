select movies.title from people
inner join stars on people.id = stars.person_id
inner join movies on stars.movie_id = movies.id
inner join ratings on ratings.movie_id = movies.id
where people.name = 'Chadwick Boseman'
order by ratings.rating desc
limit 5;