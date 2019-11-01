from app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4670, debug=True)


# Flask Application Assignment
#
# • Create a flask application that connects to pgAdmin’s database that you created for this app
# • Create a form that allows you to look up a customer by their name and displays the cars they
# own
# • Create a page that displays all inventory for products that the company owns
# • Create a page that allows a user who is logged in to add maintenance records to the database.
# The form should ask for all fields required by the database table
