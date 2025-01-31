# Python Standard Library
import sqlite3
from typing import Dict, Any, List





def get_id_current_series(db: str) -> int:
    """
    Fetch the ID of the current film series.

    Args:
        db (str): Name of the database to query.

    Returns:
        int: ID of the current film series.
    """
    # Create connection and cursor
    connection = sqlite3.connect(db, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Query db
    query = "SELECT series_id FROM series ORDER BY series_id DESC LIMIT 1;"
    cursor.execute(query)
    current_series_id = cursor.fetchone()
    
    # Close cursor and connection
    cursor.close()
    connection.close()

    return current_series_id


def get_info_series(db: str, series_id: int) -> Dict[str, Any]:
    """
    Fetch information about a specific series.

    Args:
        db (str): Name of the database to query.
        series_id (int): ID of the series to fetch.

    Returns:
        Dict[str, Any]: Information about the series.
    """
    # Create connection and cursor
    connection = sqlite3.connect(db, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Query db
    query = "SELECT s.series_id, "
    query = query + "series_semester || series_year AS semester, "
    query = query + "series_semester, "
    query = query + "series_year, "
    query = query + "series_title, "
    query = query + "series_brief, "
    query = query + "series_poster, "
    query = query + "series_poster_url, "
    query = query + "series_display, "
    query = query + "color1, "
    query = query + "color2, "
    query = query + "color3 "
    query = query + "FROM series s "
    query = query + "JOIN colors AS c ON s.series_id = c.series_id "
    query = query + "WHERE s.series_id = ?; "
    cursor.execute(query, (series_id,))
    results = cursor.fetchone()

    # Close cursor and connection
    cursor.close()
    connection.close()

    return dict(results)


def get_info_schedules(db: str, series_id: int) -> List[Dict[str, Any]]:
    """
    Fetch information about the schedules of a specific series.

    Args:
        db (str): Name of the database to query.
        series_id (int): ID of the series to fetch schedules for.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing schedule information.
    """
    # Create connection and cursor
    connection = sqlite3.connect(db, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Query db
    query = "SELECT strftime('%d', schedule) AS day, "
    query = query + "f.id, "
    query = query + "rtrim (substr ('January  February March    April    May      June     July     August   SeptemberOctober  November December', strftime ('%m', schedule) * 9 - 8, 9)) AS month, "
    query = query + "film_title, film_director, film_year, film_runtime, wiki, sc.schedule, sc.notes "
    query = query + "FROM series AS se "
    query = query + "JOIN schedules AS sc ON se.series_id = sc.series_id "
    query = query + "JOIN films AS f ON sc.film_id = f.id "
    query = query + "WHERE se.series_id = ?; "
    cursor.execute(query, (series_id,))

    # Get rows
    rows = cursor.fetchall()

    # Get the column names from cursor.description
    columns = [column[0] for column in cursor.description]

    # Convert each row into a dictionary using zip
    result = [dict(zip(columns, row)) for row in rows]

    # Close cursor and connection
    cursor.close()
    connection.close()

    return result


def get_info_series_ids(db: str) -> List[Dict[str, Any]]:
    """
    Fetch information of all series IDs.

    Args:
        db (str): Name of the database to query.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing series ID information.
    """
    # Create connection and cursor
    connection = sqlite3.connect(db, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Query db
    query = "SELECT DISTINCT(series_id), series_semester, series_year, series_display FROM series; "
    cursor.execute(query)

    # Get rows
    rows = cursor.fetchall()

    # Get the column names from cursor.description
    columns = [column[0] for column in cursor.description]

    # Convert each row into a dictionary using zip
    result = [dict(zip(columns, row)) for row in rows]

    return result


def get_info_serieses(db: str) -> List[Dict[str, Any]]:
    """
    Fetch information of all series IDs.

    Args:
        db (str): Name of the database to query.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing series ID information.
    """
    # Create connection and cursor
    connection = sqlite3.connect(db, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Query db
    query = "SELECT DISTINCT(series_id), "
    query = query + "series_semester, "
    query = query + "series_year, "
    query = query + "series_display " 
    query = query + "FROM series; "
    cursor.execute(query)

    # Get rows
    rows = cursor.fetchall()

    # Get the column names from cursor.description
    columns = [column[0] for column in cursor.description]

    # Convert each row into a dictionary using zip
    result = [dict(zip(columns, row)) for row in rows]

    return result


def get_info_film(db: str, film_id: int) -> Dict[str, Any]:
    """
    Fetch information about a specific film.

    Args:
        db (str): Name of the database to query.
        film_id (int): ID of the film to fetch.

    Returns:
        Dict[str, Any]: Information about the film.
    """
    # Create connection and cursor
    connection = sqlite3.connect(db, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Query db
    query = "SELECT * "
    query = query + "FROM films "
    query = query + "WHERE id = ?; "
    cursor.execute(query, (film_id,))

    # Get row
    row = cursor.fetchone()

    # Convert row into a dictionary
    result = dict(row)

    return result
