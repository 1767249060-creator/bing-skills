import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parents[3]
    / "skill-discovery-optimizer"
    / "scripts"
    / "verify_publish.py"
)
SPEC = importlib.util.spec_from_file_location("verify_publish", MODULE_PATH)
verify = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(verify)


class VerifyPublishTest(unittest.TestCase):
    def test_listing_url(self):
        self.assertEqual(
            verify.listing_url("Bing-Bryan/skills-by-bing", "xianyu-publish"),
            "https://www.skills.sh/Bing-Bryan/skills-by-bing/xianyu-publish",
        )

    def test_soft_404_with_200_is_rejected(self):
        body = "<title>xianyu-publish — bing-bryan/skills-by-bing</title>This page could not be found"
        self.assertFalse(verify.page_is_listing(200, "https://www.skills.sh/example", body))

    def test_real_detail_markers_are_accepted(self):
        body = "Installation Installs Repository First Seen Security Audits"
        self.assertTrue(verify.page_is_listing(200, "https://www.skills.sh/example", body))

    def test_wrong_host_or_status_is_rejected(self):
        body = "Installation Installs Repository First Seen"
        self.assertFalse(verify.page_is_listing(404, "https://www.skills.sh/example", body))
        self.assertFalse(verify.page_is_listing(200, "https://example.com/skill", body))


if __name__ == "__main__":
    unittest.main()
