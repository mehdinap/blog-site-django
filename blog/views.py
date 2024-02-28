from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains_ONE",
        "image": "Untitled.jpeg",
        "author": "Mehdi",
        "date": date(2024, 2, 20),
        "title": "Hacking Systems:!_ONE",
        "excerpt": "At the time for hacking system!",
        "content": """
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Asperiores, commodi. Aspernatur itaque magni in alias voluptas, sed ratione dolores impedit modi laudantium doloribus inventore accusamus. Maxime omnis ex ullam quae!

        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Asperiores, commodi. Aspernatur itaque magni in alias voluptas, sed ratione dolores impedit modi laudantium doloribus inventore accusamus. Maxime omnis ex ullam quae!

        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Asperiores, commodi. Aspernatur itaque magni in alias voluptas, sed ratione dolores impedit modi laudantium doloribus inventore accusamus. Maxime omnis ex ullam quae!
        """,
    },
    {
        "slug": "hike-in-the-mountains_TWO",
        "image": "1.jpeg",
        "author": "Mehdi",
        "date": date(2024, 2, 10),
        "title": "Hacking Systems:!_TWO",
        "excerpt": "At the time for hacking system!",
        "content": """
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Asperiores, commodi. Aspernatur itaque magni in alias voluptas, sed ratione dolores impedit modi laudantium doloribus inventore accusamus. Maxime omnis ex ullam quae!

        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Asperiores, commodi. Aspernatur itaque magni in alias voluptas, sed ratione dolores impedit modi laudantium doloribus inventore accusamus. Maxime omnis ex ullam quae!

        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Asperiores, commodi. Aspernatur itaque magni in alias voluptas, sed ratione dolores impedit modi laudantium doloribus inventore accusamus. Maxime omnis ex ullam quae!
        """,
    },
    {
        "slug": "hike-in-the-mountains_THREE",
        "image": "2.jpeg",
        "author": "Mehdi",
        "date": date(2024, 2, 4),
        "title": "Hacking Systems:!_THREE",
        "excerpt": "At the time for hacking system!",
        "content": """
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Asperiores, commodi. Aspernatur itaque magni in alias voluptas, sed ratione dolores impedit modi laudantium doloribus inventore accusamus. Maxime omnis ex ullam quae!

        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Asperiores, commodi. Aspernatur itaque magni in alias voluptas, sed ratione dolores impedit modi laudantium doloribus inventore accusamus. Maxime omnis ex ullam quae!

        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Asperiores, commodi. Aspernatur itaque magni in alias voluptas, sed ratione dolores impedit modi laudantium doloribus inventore accusamus. Maxime omnis ex ullam quae!
        """,
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "3.jpeg",
        "author": "Mehdi",
        "date": date(2024, 2, 3),
        "title": "Hacking Systems:!",
        "excerpt": "At the time for hacking system!DUUUUEEEE",
        "content": """
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Asperiores, commodi. Aspernatur itaque magni in alias voluptas, sed ratione dolores impedit modi laudantium doloribus inventore accusamus. Maxime omnis ex ullam quae!

        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Asperiores, commodi. Aspernatur itaque magni in alias voluptas, sed ratione dolores impedit modi laudantium doloribus inventore accusamus. Maxime omnis ex ullam quae!

        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Asperiores, commodi. Aspernatur itaque magni in alias voluptas, sed ratione dolores impedit modi laudantium doloribus inventore accusamus. Maxime omnis ex ullam quae!
        """,
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "Untitled.jpeg",
        "author": "Mehdi",
        "date": date(2024, 2, 1),
        "title": "Hacking Systems:!NEW",
        "excerpt": "At the time for hacking system!",
        "content": """
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Asperiores, commodi. Aspernatur itaque magni in alias voluptas, sed ratione dolores impedit modi laudantium doloribus inventore accusamus. Maxime omnis ex ullam quae!

        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Asperiores, commodi. Aspernatur itaque magni in alias voluptas, sed ratione dolores impedit modi laudantium doloribus inventore accusamus. Maxime omnis ex ullam quae!

        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Asperiores, commodi. Aspernatur itaque magni in alias voluptas, sed ratione dolores impedit modi laudantium doloribus inventore accusamus. Maxime omnis ex ullam quae!
        """,
    },
]


def get_date(post):
    return post["date"]


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_post = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_post})


def posts(request):
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {"post": identified_post})
