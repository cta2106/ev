import sqlite3
from datetime import datetime
from typing import List

from langchain.agents import tool

from constants import DB_NAME
from customer import Customer


@tool
def record_customer_data(
        first_name: str,
        last_name: str,
        email: str,
        street: str,
        city: str,
        state: str,
        zip_code: str,
        email_consent: bool,
        concerns: List[str],
) -> Customer:
    """
    Record customer information once all information is available.
    """
    customer = Customer(
        first_name=first_name,
        last_name=last_name,
        email=email,
        street=street,
        city=city,
        state=state,
        zip_code=zip_code,
        email_consent=email_consent,
        concerns=concerns,
    )

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO customers (first_name, last_name, email, street, city, state, zip_code, country, email_consent, concerns)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                customer.first_name,
                customer.last_name,
                customer.email,
                customer.street,
                customer.city,
                customer.state,
                customer.zip_code,
                customer.country,
                customer.email_consent,
                ", ".join(customer.concerns),
            ),
        )
        conn.commit()
        conn.close()
    except:
        return "Customer already recorded"

    return customer


# ToDo: Complete this function

@tool
def suggest_dealership(zip_code: str, concerns: List[str]) -> str:
    """
    Suggests a dealership based on the customer's zip code and concerns.
    For now, it suggests the Tesla dealership in Boston regardless of the input.
    """
    dealership_address = "Tesla Dealership, 888 Boylston St, Boston, MA"

    return dealership_address


# ToDo: Complete this function
@tool
def schedule_meeting(date: datetime, dealership_name: str) -> str:
    """
    Schedules a meeting at the specified dealership on the given date.
    Currently, this is a placeholder function that always confirms the meeting.
    """
    # Placeholder confirmation message
    confirmation_message = f"Meeting scheduled at {dealership_name} on {date.strftime('%Y-%m-%d %H:%M:%S')}."

    # In a real scenario, we would add logic to check availability,
    # interact with a calendar service, or store the meeting details in a database.

    return confirmation_message


tools = [record_customer_data, suggest_dealership, schedule_meeting]
