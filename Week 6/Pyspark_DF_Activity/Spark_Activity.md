# Spark Activity

## Goal
- Practice working with Spark Dataframes

## Steps
- Download the following csv files and load them into Spark Dataframes:
    - rental.csv
    - payment.csv
    - inventory.csv
    - film.csv
    - customer.csv

- Using dataframe transformations, answer the following questions. Be sure to record the transformations you used for review purposes.
    - Who are the top 5 customers for our movie rental store?
    - What are the top 5 movies that produce the most revenue for our store?
        ```
              SELECT f.title, round(sum(ceil(date_diff(r.return_date, r.rental_date) / f.rental_duration) * f.rental_rate), 2) amount_spent
            FROM film f JOIN inventory i ON f.film_id = i.film_id 
            JOIN rental r ON i.inventory_id = r.inventory_id
            GROUP BY f.title ORDER BY amount_spent DESC LIMIT 5;
        ```

    - Based on our current inventory of films and the rentals that we get, should we modify our inventory at all? How so?

## Review
- We will review later today.
