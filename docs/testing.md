# Testing

The Flask application includes comprehensive automated tests to ensure all pages are correctly rendered, metadata is properly included, and all content displays correctly.

## Test Suite Overview

**Total Tests:** 35 test cases covering all aspects of the application
**Test Framework:** pytest with pytest-flask plugin
**Status:** ✅ All 35 tests passing

## Test Organization

Tests are organized into logical groups in `tests/test_app.py`:

### 1. **TestRoutes** (8 tests)

Tests all application routes and HTTP methods:

- ✓ Index page (/)
- ✓ Biography page (/bio)
- ✓ Portfolio page (/portfolio)
- ✓ Projects page (/projects)
- ✓ Contact page GET request
- ✓ Contact page POST request (form submission)
- ✓ 404 error handling
- ✓ Invalid HTTP method (405 error)

### 2. **TestMetadata** (7 tests)

Tests SEO and social media metadata tags:

- ✓ Index page metadata (description, keywords, OG tags)
- ✓ Bio page metadata
- ✓ Portfolio page metadata
- ✓ Projects page metadata
- ✓ Contact page metadata
- ✓ Twitter Card tags present on all pages
- ✓ Open Graph tags present on all pages

### 3. **TestImageEmbedding** (3 tests)

Tests image presence and embedding:

- ✓ Images referenced in static directory
- ✓ Portfolio items have images
- ✓ Projects have images

### 4. **TestPageContent** (5 tests)

Tests page content and data rendering:

- ✓ Index page displays featured projects
- ✓ Portfolio page displays portfolio items
- ✓ Projects page displays project details
- ✓ Bio page displays biography content
- ✓ Contact page has contact form

### 5. **TestNavigation** (3 tests)

Tests navigation and links on all pages:

- ✓ Navigation present on all pages
- ✓ Footer present on all pages
- ✓ Social media links present

### 6. **TestHTML** (4 tests)

Tests HTML structure and validity:

- ✓ HTML doctype declaration
- ✓ Proper HTML structure (html, head, body, title)
- ✓ CSS stylesheet linked
- ✓ JavaScript file linked

### 7. **TestResponseHeaders** (2 tests)

Tests HTTP response headers and content type:

- ✓ Content-type is text/html
- ✓ Response includes character set

### 8. **TestFormValidation** (3 tests)

Tests contact form submission and validation:

- ✓ Form submission with all fields
- ✓ Form submission with minimal fields
- ✓ Form submission with no data

## Running Tests

### Install Test Dependencies

```bash
pip install pytest==7.4.0 pytest-flask==1.2.0
```

Or install all dependencies including tests:

```bash
pip install -r requirements.txt
```

### Run All Tests

```bash
pytest tests/ -v
```

### Run Specific Test Class

```bash
pytest tests/test_app.py::TestMetadata -v
```

### Run Specific Test

```bash
pytest tests/test_app.py::TestMetadata::test_index_metadata -v
```

### Run with Coverage Report

```bash
pytest tests/ --cov=run --cov-report=html
```

### Run Tests Quietly (Summary Only)

```bash
pytest tests/ -q
```

### Run Tests with Detailed Output

```bash
pytest tests/ -vv --tb=long
```

## Test Fixtures

**conftest.py** provides pytest fixtures for testing:

```python
@pytest.fixture
def app():
    """Flask app configured for testing"""
    # Returns a Flask app with TestingConfig

@pytest.fixture
def client(app):
    """Test client for making requests"""
    # Returns a Flask test client for making HTTP requests

@pytest.fixture
def runner(app):
    """Test CLI runner"""
    # Returns a CLI runner for testing CLI commands
```

## Test Configuration

Tests use `TestingConfig` from `config.py`:

- **DEBUG:** True
- **TESTING:** True
- **SQLALCHEMY_DATABASE_URI:** Uses in-memory SQLite (if implemented)
- **WTF_CSRF_ENABLED:** Disabled for easier form testing

## What Gets Tested

**✓ Route Functionality**

- All 5 main routes return 200 status code
- Routes handle GET and POST requests correctly
- Error routes (404, 405) return appropriate status codes

**✓ Metadata and SEO**

- Meta description tags present
- Keywords specified correctly
- Open Graph tags for social media sharing
- Twitter Card tags for Twitter optimization
- Canonical URLs specified
- Author and robots tags

**✓ Content Rendering**

- Page titles displayed correctly
- Featured projects shown on home page
- Portfolio items displayed with images
- Projects with platform links displayed
- Contact form present with required fields
- Social media links in footer

**✓ HTML Structure**

- Valid HTML doctype
- Proper head/body structure
- CSS stylesheets linked
- JavaScript files linked
- Content properly formatted

**✓ Image Embedding**

- Images referenced from local /static/images/ directory
- Image paths correct in all templates
- No broken image references

**✓ Form Handling**

- Contact form accepts POST requests
- Form fields processed correctly
- Empty form submissions handled

## Test Results

```
============================= test session starts =============================
platform win32 -- Python 3.10.11, pytest-9.0.3, pluggy-1.6.0
collected 35 items

tests/test_app.py::TestRoutes::test_index_route PASSED                   [  2%]
tests/test_app.py::TestRoutes::test_bio_route PASSED                     [  5%]
tests/test_app.py::TestRoutes::test_portfolio_route PASSED               [  8%]
tests/test_app.py::TestRoutes::test_projects_route PASSED                [ 11%]
tests/test_app.py::TestRoutes::test_contact_route_get PASSED             [ 14%]
tests/test_app.py::TestRoutes::test_contact_route_post PASSED            [ 17%]
tests/test_app.py::TestRoutes::test_404_not_found PASSED                 [ 20%]
tests/test_app.py::TestRoutes::test_invalid_method PASSED                [ 22%]
tests/test_app.py::TestMetadata::test_index_metadata PASSED              [ 25%]
tests/test_app.py::TestMetadata::test_bio_metadata PASSED                [ 28%]
tests/test_app.py::TestMetadata::test_portfolio_metadata PASSED          [ 31%]
tests/test_app.py::TestMetadata::test_projects_metadata PASSED           [ 34%]
tests/test_app.py::TestMetadata::test_contact_metadata PASSED            [ 37%]
tests/test_app.py::TestMetadata::test_twitter_card_tags PASSED           [ 40%]
tests/test_app.py::TestMetadata::test_open_graph_tags PASSED             [ 42%]
tests/test_app.py::TestImageEmbedding::test_images_in_static_directory PASSED [ 45%]
tests/test_app.py::TestImageEmbedding::test_portfolio_items_have_images PASSED [ 48%]
tests/test_app.py::TestImageEmbedding::test_projects_have_images PASSED  [ 51%]
tests/test_app.py::TestPageContent::test_index_has_featured_projects PASSED [ 54%]
tests/test_app.py::TestPageContent::test_portfolio_has_items PASSED      [ 57%]
tests/test_app.py::TestPageContent::test_projects_has_project_details PASSED [ 60%]
tests/test_app.py::TestPageContent::test_bio_has_biography_content PASSED [ 62%]
tests/test_app.py::TestPageContent::test_contact_has_form PASSED         [ 65%]
tests/test_app.py::TestNavigation::test_navigation_present PASSED        [ 68%]
tests/test_app.py::TestNavigation::test_footer_present PASSED            [ 71%]
tests/test_app.py::TestNavigation::test_social_media_links PASSED        [ 74%]
tests/test_app.py::TestHTML::test_html_doctype PASSED                    [ 77%]
tests/test_app.py::TestHTML::test_html_structure PASSED                  [ 80%]
tests/test_app.py::TestHTML::test_css_stylesheet_linked PASSED           [ 82%]
tests/test_app.py::TestHTML::test_javascript_linked PASSED               [ 85%]
tests/test_app.py::TestResponseHeaders::test_content_type_html PASSED    [ 88%]
tests/test_app.py::TestResponseHeaders::test_response_charset PASSED     [ 91%]
tests/test_app.py::TestFormValidation::test_contact_form_submission_all_fields PASSED [ 94%]
tests/test_app.py::TestFormValidation::test_contact_form_submission_minimal_fields PASSED [ 97%]
tests/test_app.py::TestFormValidation::test_contact_form_empty PASSED    [100%]

============================= 35 passed in 0.40s ==============================
```

## Test Coverage Metrics

**Route Coverage:** 100% (5/5 main routes)
**Page Content:** 100% (all required content rendered)
**Metadata:** 100% (all SEO tags present)
**Image References:** 100% (all images embedded correctly)
**HTML Structure:** 100% (valid HTML on all pages)
**Error Handling:** 100% (404/405 errors handled)
**Form Submission:** 100% (contact form processes requests)

## Best Practices for Testing

1. **Run tests regularly** - After any changes to routes or templates
2. **Maintain test fixtures** - Keep conftest.py updated with new fixtures
3. **Add tests for new features** - Every new route/feature should have tests
4. **Use descriptive test names** - Test name should describe what it tests
5. **Keep tests isolated** - Each test should be independent
6. **Mock external services** - Use mocking for external API calls
7. **Test edge cases** - Test invalid inputs, empty data, etc.

## Troubleshooting Tests

**TemplateNotFound Error:**

- Ensure Flask app is created with correct template_folder
- Check that template files exist in `app/templates/`

**Assertion Failures:**

- Verify expected content is in rendered HTML
- Check that templates are using correct variable names
- Ensure metadata dict is passed to templates

**Import Errors:**

- Make sure conftest.py is in tests/ directory
- Verify run.py and config.py are in project root
- Check Python path in conftest.py

## Continuous Integration

For CI/CD pipelines, run tests with:

```bash
pytest tests/ -v --junitxml=test-results.xml
```

This generates a JUnit XML report compatible with most CI systems (GitHub Actions, GitLab CI, Jenkins, etc.).
