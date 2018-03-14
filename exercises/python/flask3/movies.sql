CREATE TABLE `movies` (
  `imdb_id` varchar(10) NOT NULL,
  `title` varchar(40) NOT NULL,
  `year` int(11) NOT NULL,
  `rating` double NOT NULL,
  `synopsis` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `movies` (`imdb_id`, `title`, `year`, `rating`, `synopsis`) VALUES
('tt0068646', 'The Godfather', 1972, 9.2, 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.'),
('tt0110912', 'Pulp Fiction', 1994, 8.9, 'The lives of two mob hit men, a boxer, a gangster\'s wife, and a pair of diner bandits intertwine in four tales of violence and redemption.'),
('tt0111161', 'The Shawshank Redemption', 1994, 9.3, 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.'),
('tt0468569', 'The Dark Knight', 2008, 8.9, ''),
('tt1375666', 'Inception', 2010, 8.8, 'A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.');

ALTER TABLE `movies`
  ADD PRIMARY KEY (`imdb_id`);