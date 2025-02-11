# Queries

## Question 1

What are the five most similar segments to segment "267:476"?

### Query

```sql
SELECT 
    title AS podcast_name,
    segment_id,
    content,
    start_time,
    end_time,
    embedding <-> (SELECT embedding FROM segment WHERE segment_id = '267:476') AS distance
FROM segment
    JOIN podcast ON podcast.podcast_id = segment.podcast_id
WHERE segment_id <> '267:476'
ORDER BY distance
LIMIT 5
```

### Result

```sql
('Podcast: Ryan Graves: UFOs, Fighter Jets, and Aliens | Lex Fridman Podcast #308', '113:2792', ' encounters, human beings, if we were to meet another alien', datetime.time(1, 52, 5, 620000), datetime.time(1, 52, 9, 860000), 0.6483450674336982)
('Podcast: Richard Dawkins: Evolution, Intelligence, Simulation, and Memes | Lex Fridman Podcast #87', '268:1019', ' Suppose we did meet an alien from outer space', datetime.time(0, 48, 20, 40000), datetime.time(0, 48, 23, 80000), 0.6558106859320757)
('Podcast: Jeffrey Shainline: Neuromorphic Computing and Optoelectronic Intelligence | Lex Fridman Podcast #225', '305:3600', ' but if we think of alien civilizations out there', datetime.time(2, 37, 59, 960000), datetime.time(2, 38, 4, 40000), 0.6595433115268592)
('Podcast: Michio Kaku: Future of Humans, Aliens, Space Travel & Physics | Lex Fridman Podcast #45', '18:464', ' So I think when we meet alien life from outer space,', datetime.time(0, 21, 56, 860000), datetime.time(0, 21, 59, 580000), 0.6662026419636159)
('Podcast: Alien Debate: Sara Walker and Lee Cronin | Lex Fridman Podcast #279', '71:989', ' because if aliens come to us', datetime.time(0, 39, 2, 340000), datetime.time(0, 39, 3, 620000), 0.6742942635162208)
```

## Question 2

What are the five most dissimilar segments to segment "267:476"?

### Query

```sql
SELECT
    title AS podcast_name,
    segment_id,
    content,
    start_time,
    end_time,
    embedding <-> (SELECT embedding FROM segment WHERE segment_id = '267:476') AS distance
FROM segment
    JOIN podcast ON podcast.podcast_id = segment.podcast_id
ORDER BY distance DESC
LIMIT 5
```

### Result

```sql
('Podcast: Jason Calacanis: Startups, Angel Investing, Capitalism, and Friendship | Lex Fridman Podcast #161', '119:218', ' a 73 Mustang Grande in gold?', datetime.time(0, 8, 39, 960000), datetime.time(0, 8, 43, 800000), 1.6157687685840119)
('Podcast: Rana el Kaliouby: Emotion AI, Social Robots, and Self-Driving Cars | Lex Fridman Podcast #322', '133:2006', ' for 94 car models.', datetime.time(1, 36, 58, 620000), datetime.time(1, 37, 0, 820000), 1.5863359073014982)
('Podcast: Travis Stevens: Judo, Olympics, and Mental Toughness | Lex Fridman Podcast #223', '283:1488', ' when I called down to get the sauna.', datetime.time(1, 1, 49, 340000), datetime.time(1, 1, 51, 100000), 1.572552805197421)
('Podcast: Jeremy Howard: fast.ai Deep Learning Courses and Research | Lex Fridman Podcast #35', '241:1436', ' which has all the courses pre-installed.', datetime.time(1, 7, 48, 900000), datetime.time(1, 7, 51, 140000), 1.5663319710412156)
('Podcast: Joscha Bach: Nature of Reality, Dreams, and Consciousness | Lex Fridman Podcast #212', '307:3933', ' and very few are first class and some are budget.', datetime.time(2, 57, 28, 640000), datetime.time(2, 57, 30, 960000), 1.5616341289820461)
```

## Question 3

What are the five most similar segments to segment "48:511"?

### Query

```sql
SELECT 
    title AS podcast_name,
    segment_id,
    content,
    start_time,
    end_time,
    embedding <-> (SELECT embedding FROM segment WHERE segment_id = '48:511') AS distance
FROM segment
    JOIN podcast ON podcast.podcast_id = segment.podcast_id
WHERE segment_id <> '48:511'
ORDER BY distance
LIMIT 5
```

### Result

```sql
('Podcast: Andrew Huberman: Neuroscience of Optimal Performance | Lex Fridman Podcast #139', '155:648', ' Is there something interesting to you or fundamental to you about the circuitry of the brain', datetime.time(1, 3, 18, 480000), datetime.time(1, 3, 25, 840000), 0.652299685331962)
('Podcast: Cal Newport: Deep Work, Focus, Productivity, Email, and Social Media | Lex Fridman Podcast #166', '61:3707', ' of what we might discover about neural networks?', datetime.time(2, 21, 38, 20000), datetime.time(2, 21, 40, 100000), 0.7121050124628524)
('Podcast: Matt Botvinick: Neuroscience, Psychology, and AI at DeepMind | Lex Fridman Podcast #106', '48:512', " And our brain is there. There's some there's quite a few differences. Are some of them to you either interesting or perhaps profound in terms of in terms of the gap we might want to try to close in trying to create a human level intelligence.", datetime.time(0, 30, 46, 840000), datetime.time(0, 31, 5, 840000), 0.7195603322334674)
('Podcast: Yann LeCun: Dark Matter of Intelligence and Self-Supervised Learning | Lex Fridman Podcast #258', '276:2642', ' Have these, I mean, small pockets of beautiful complexity. Does that, do cellular automata, do these kinds of emergence and complex systems give you some intuition or guide your understanding of machine learning systems and neural networks and so on?', datetime.time(2, 23, 48, 160000), datetime.time(2, 24, 6, 160000), 0.7357217735737499)
('Podcast: Stephen Wolfram: Fundamental Theory of Physics, Life, and the Universe | Lex Fridman Podcast #124', '2:152', ' So is there something like that with physics where so deep learning neural networks have been around for a long time?', datetime.time(0, 10, 10, 860000), datetime.time(0, 10, 18, 860000), 0.7366969553372291)
```

## Question 4

What are the five most similar segments to segment "51:56"?

### Query

```sql
SELECT 
    title AS podcast_name,
    segment_id,
    content,
    start_time,
    end_time,
    embedding <-> (SELECT embedding FROM segment WHERE segment_id = '51:56') AS distance
FROM segment
    JOIN podcast ON podcast.podcast_id = segment.podcast_id
WHERE segment_id <> '51:56'
ORDER BY distance
LIMIT 5
```

### Result

```sql
('Podcast: George Hotz: Hacking the Simulation & Learning to Drive with Neural Nets | Lex Fridman Podcast #132', '308:144', " I mean, we don't understand dark energy, right?", datetime.time(0, 8, 20, 440000), datetime.time(0, 8, 22, 600000), 0.6681965222094363)
('Podcast: Lex Fridman: Ask Me Anything - AMA January 2021 | Lex Fridman Podcast', '243:273', " Like, what's up with this dark matter and dark energy stuff?", datetime.time(0, 15, 46, 220000), datetime.time(0, 15, 50, 120000), 0.7355511762966292)
('Podcast: Katherine de Kleer: Planets, Moons, Asteroids & Life in Our Solar System | Lex Fridman Podcast #184', '196:685', ' being like, what the hell is dark matter and dark energy?', datetime.time(0, 43, 11, 720000), datetime.time(0, 43, 15, 960000), 0.7631141596843518)
('Podcast: Alex Filippenko: Supernovae, Dark Energy, Aliens & the Expanding Universe | Lex Fridman Podcast #137', '51:36', ' Do we have any understanding of what the heck that thing is?', datetime.time(0, 3, 36), datetime.time(0, 3, 39), 0.7922019445543276)
('Podcast: Leonard Susskind: Quantum Mechanics, String Theory and Black Holes | Lex Fridman Podcast #41', '122:831', ' That is a big question in physics right now.', datetime.time(0, 39, 34, 900000), datetime.time(0, 39, 37, 620000), 0.8022704628640559)
```

## Question 5

For each of the following segments, find the five most similar podcast episodes.

### Query

```sql
WITH ranked_podcasts AS (
    SELECT 
        p.title,
        '267:476' AS segment_id,
        AVG(s.embedding <-> (SELECT temp.embedding FROM segment temp WHERE temp.segment_id = '267:476')) AS avg_distance,
        RANK() OVER (PARTITION BY '267:476' ORDER BY 
            AVG(s.embedding <-> (SELECT temp.embedding FROM segment temp WHERE temp.segment_id = '267:476'))
        ASC) AS rank
    FROM podcast p
    JOIN segment s ON s.podcast_id = p.podcast_id
    GROUP BY p.title

    UNION ALL

    SELECT 
        p.title,
        '48:511' AS segment_id,
        AVG(s.embedding <-> (SELECT temp.embedding FROM segment temp WHERE temp.segment_id = '48:511')) AS avg_distance,
        RANK() OVER (PARTITION BY '48:511' ORDER BY 
            AVG(s.embedding <-> (SELECT temp.embedding FROM segment temp WHERE temp.segment_id = '48:511'))
        ASC) AS rank
    FROM podcast p
    JOIN segment s ON s.podcast_id = p.podcast_id
    GROUP BY p.title

    UNION ALL

    SELECT 
        p.title,
        '51:56' AS segment_id,
        AVG(s.embedding <-> (SELECT temp.embedding FROM segment temp WHERE temp.segment_id = '51:56')) AS avg_distance,
        RANK() OVER (PARTITION BY '51:56' ORDER BY 
            AVG(s.embedding <-> (SELECT temp.embedding FROM segment temp WHERE temp.segment_id = '51:56'))
        ASC) AS rank
    FROM podcast p
    JOIN segment s ON s.podcast_id = p.podcast_id
    GROUP BY p.title
)

SELECT segment_id, title, avg_distance
FROM ranked_podcasts
WHERE rank <= 5
ORDER BY segment_id, rank
```

### Result

```sql
('267:476', 'Podcast: Sara Walker: The Origin of Life on Earth and Alien Worlds | Lex Fridman Podcast #198', 1.1639073436635057)
('267:476', 'Podcast: Nick Bostrom: Simulation and Superintelligence | Lex Fridman Podcast #83', 1.1656388026024265)
('267:476', 'Podcast: Alex Filippenko: Supernovae, Dark Energy, Aliens & the Expanding Universe | Lex Fridman Podcast #137', 1.169184164010911)
('267:476', 'Podcast: Steven Pinker: AI in the Age of Reason | Lex Fridman Podcast #3', 1.1709406061025283)
('267:476', 'Podcast: David Chalmers: The Hard Problem of Consciousness | Lex Fridman Podcast #69', 1.1714010144134988)
('48:511', 'Podcast: Matt Botvinick: Neuroscience, Psychology, and AI at DeepMind | Lex Fridman Podcast #106', 1.1273541527330924)
('48:511', 'Podcast: Christof Koch: Consciousness | Lex Fridman Podcast #2', 1.1391818856346418)
('48:511', 'Podcast: Dileep George: Brain-Inspired AI | Lex Fridman Podcast #115', 1.1452330612614703)
('48:511', 'Podcast: Tomaso Poggio: Brains, Minds, and Machines | Lex Fridman Podcast #13', 1.1509146574515634)
('48:511', 'Podcast: Jitendra Malik: Computer Vision | Lex Fridman Podcast #110', 1.1553830701332357)
('51:56', 'Podcast: Sean Carroll: Quantum Mechanics and the Many-Worlds Interpretation | Lex Fridman Podcast #47', 1.1410222538303005)
('51:56', 'Podcast: Stephen Wolfram: Fundamental Theory of Physics, Life, and the Universe | Lex Fridman Podcast #124', 1.1597211582221392)
('51:56', 'Podcast: Alex Filippenko: Supernovae, Dark Energy, Aliens & the Expanding Universe | Lex Fridman Podcast #137', 1.1718329100463998)
('51:56', 'Podcast: Cumrun Vafa: String Theory | Lex Fridman Podcast #204', 1.1769855214736251)
('51:56', 'Podcast: Donald Hoffman: Reality is an Illusion - How Evolution Hid the Truth | Lex Fridman Podcast #293', 1.1785260521872498)
```

## Question 6

For podcast episode id = VeH7qKZr0WI, find the five most similar podcast episodes.

### Query

```sql
WITH podcast_avgs AS (
    SELECT
        p.podcast_id,
        p.title,
        AVG(s.embedding) AS avg_embedding
    FROM podcast p
        JOIN segment s ON s.podcast_id = p.podcast_id
    GROUP BY p.podcast_id, p.title
)

SELECT
    podcast_avgs.title,
    podcast_avgs.avg_embedding <-> (SELECT temp.avg_embedding FROM podcast_avgs temp WHERE temp.podcast_id = 'VeH7qKZr0WI') AS distance
FROM podcast_avgs
WHERE podcast_avgs.podcast_id <> 'VeH7qKZr0WI'
ORDER BY distance
LIMIT 5
```

### Result

```sql
('Podcast: Tyler Cowen: Economic Growth & the Fight Against Conformity & Mediocrity | Lex Fridman Podcast #174', 0.11950103776872197)
('Podcast: Eric Weinstein: Difficult Conversations, Freedom of Speech, and Physics | Lex Fridman Podcast #163', 0.1257139025632404)
('Podcast: Michael Malice and Yaron Brook: Ayn Rand, Human Nature, and Anarchy | Lex Fridman Podcast #178', 0.12842690324343972)
('Podcast: Steve Keen: Marxism, Capitalism, and Economics | Lex Fridman Podcast #303', 0.12916269225753493)
('Podcast: Michael Malice: The White Pill, Freedom, Hope, and Happiness Amidst Chaos | Lex Fridman Podcast #150', 0.13040864953585687)
```
