from sqlalchemy import text


def test_for_db_connection(app, db):
    with app.app_context():
        try:
            db.session.execute(text('SELECT 1'))
            print('Connection successful !')
        except Exception as e:
            print('Connection failed ! ERROR : ', e)

