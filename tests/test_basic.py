import pytest
from project_code import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_app_starts(client):
    """Check if the app is created successfully."""
    assert client is not None


def test_home_page_redirect(client):
    """Check if the home page (/) redirects to the product list (Status 302)."""
    response = client.get('/')
    assert response.status_code == 302 


def test_secret_key_is_set():
    """Check if the secret key is correctly loaded for sessions."""
    app = create_app()
    assert app.secret_key == 'shopease_secret_key_123'


def test_404_page(client):
    """Check that a non-existent URL returns a 404 error."""
    response = client.get('/this-page-does-not-exist')
    assert response.status_code == 404



def test_blueprints_registered():
    """Check if the crucial blueprints are registered in the app."""
    app = create_app()
    
    assert 'product_routes' in app.blueprints
    assert 'user_routes' in app.blueprints
    assert 'cart_routes' in app.blueprints
    assert 'order_routes' in app.blueprints


def test_cache_headers(client):
    """Check if the app sends No-Cache headers (security requirement)."""
    response = client.get('/')

    assert 'Cache-Control' in response.headers
    assert 'no-cache' in response.headers['Cache-Control']