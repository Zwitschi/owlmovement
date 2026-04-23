"""
Static HTML generation script for the Corey Pellizzi website.

Converts the Flask application to a static site with all pages,
images, CSS, and JavaScript generated as standalone HTML files.

Usage:
    python generate_static.py
    
This creates a 'build/' directory with all generated static HTML files.
"""
import os
import shutil
from pathlib import Path

from run import create_app


def generate_static_site():
    """Generate static HTML files from Flask application."""

    # Create Flask app
    app = create_app()

    # Build directory
    build_dir = Path('build')

    # Clean build directory if it exists
    if build_dir.exists():
        print(f"🗑️  Cleaning existing build directory: {build_dir}")
        shutil.rmtree(build_dir)

    # Create build directory structure
    build_dir.mkdir(parents=True, exist_ok=True)
    static_dir = build_dir / 'static'
    static_dir.mkdir(parents=True, exist_ok=True)

    print(f"📁 Created build directory structure at: {build_dir.absolute()}")

    # Define routes to generate (excluding POST-only routes)
    routes = {
        '/': 'index.html',
        '/bio': 'bio.html',
        '/portfolio': 'portfolio.html',
        '/projects': 'projects.html',
        '/contact': 'contact.html',
    }

    # Generate static HTML files
    print("\n🔨 Generating static HTML pages...")
    print("-" * 60)

    with app.test_client() as client:
        generated_count = 0

        for route, filename in routes.items():
            try:
                # Get the page content
                response = client.get(route)

                if response.status_code == 200:
                    # Write HTML file
                    html_path = build_dir / filename
                    html_path.write_text(response.data.decode('utf-8'))

                    print(
                        f"✓ {route:20} → {filename:25} ({len(response.data):,} bytes)")
                    generated_count += 1
                else:
                    print(f"✗ {route:20} → Error {response.status_code}")

            except Exception as e:
                print(f"✗ {route:20} → Error: {str(e)}")

    print("-" * 60)
    print(f"\n✅ Generated {generated_count} static HTML pages")

    # Copy static assets
    print("\n📦 Copying static assets...")
    print("-" * 60)

    source_static = Path('app/static')

    if source_static.exists():
        # Copy CSS
        css_source = source_static / 'css'
        if css_source.exists():
            css_dest = static_dir / 'css'
            shutil.copytree(css_source, css_dest, dirs_exist_ok=True)
            print(
                f"✓ Copied CSS files: {len(list(css_dest.glob('*')))} file(s)")

        # Copy JavaScript
        js_source = source_static / 'js'
        if js_source.exists():
            js_dest = static_dir / 'js'
            shutil.copytree(js_source, js_dest, dirs_exist_ok=True)
            print(
                f"✓ Copied JavaScript files: {len(list(js_dest.glob('*')))} file(s)")

        # Copy images
        img_source = source_static / 'images'
        if img_source.exists():
            img_dest = static_dir / 'images'
            shutil.copytree(img_source, img_dest, dirs_exist_ok=True)
            image_count = len(list(img_dest.glob('*')))
            total_size = sum(
                f.stat().st_size for f in img_dest.glob('*') if f.is_file())
            print(
                f"✓ Copied image files: {image_count} file(s) (~{total_size / 1024 / 1024:.2f} MB)")

    print("-" * 60)

    # Generate summary
    print("\n📊 Generation Summary")
    print("=" * 60)

    # Calculate build directory size
    total_size = sum(
        f.stat().st_size for f in build_dir.rglob('*') if f.is_file())
    file_count = len(list(build_dir.rglob('*')))

    print(f"Build directory: {build_dir.absolute()}")
    print(f"Total files: {file_count}")
    print(f"Total size: {total_size / 1024 / 1024:.2f} MB")
    print(f"\nGenerated files:")

    # List all generated files
    for item in sorted(build_dir.rglob('*')):
        if item.is_file():
            rel_path = str(item.relative_to(build_dir))
            size = item.stat().st_size
            print(f"  - {rel_path:50} ({size:,} bytes)")

    print("\n" + "=" * 60)
    print("✅ Static site generation complete!")
    print(f"\nTo serve the static site locally:")
    print(f"  python -m http.server 8000 --directory build/")
    print(f"\nThen open: http://localhost:8000/")
    print("=" * 60 + "\n")


if __name__ == '__main__':
    generate_static_site()
