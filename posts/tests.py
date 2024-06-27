from http import HTTPStatus

from django.test import TestCase

from .models import Post

# Create your tests here.


class PostModelTest(TestCase):
    def test_post_model_exist(self):
        posts = Post.objects.count()

        self.assertEqual(posts, 0)

    def test_string_rep_of_objects(self):
        post = Post.objects.create(title="Test Post", body="Test Body")

        self.assertEqual(str(post), post.title)


class HomePageTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(
            title="sample post 1",
            body="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        )
        Post.objects.create(
            title="sample post 2",
            body="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        )

    def test_homepage_returns_correct_response(self):
        response = self.client.get("/")

        self.assertTemplateUsed(response, "posts/index.html")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_homepage_return_post_list(self):
        response = self.client.get("/")

        self.assertContains(response, "sample post 1")
        self.assertContains(response, "sample post 2")


class DetailPageTest(TestCase):
    def setUp(self) -> None:
        self.post = Post.objects.create(
            title="Learn react the easy way",
            body="This is a step by step guide to learning react and nextjs",
        )

    def test_detail_page_returns_correct_response(self):
        response = self.client.get(self.post.get_absolute_url())

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "posts/detail.html")

    def test_detail_page_returns_correct_content(self):
        response = self.client.get(self.post.get_absolute_url())

        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.body)
        self.assertContains(response, self.post.created_at)
