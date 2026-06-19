import unittest
from core.chunker import chunk_text

class TestChunkText(unittest.TestCase):
    def test_empty_text(self):
        self.assertEqual(chunk_text("", chunk_size=10, chunk_overlap=2), [])

    def test_short_text(self):
        self.assertEqual(chunk_text("hello", chunk_size=10, chunk_overlap=2), ["hello"])

    def test_exact_chunk_size(self):
        self.assertEqual(chunk_text("hellohello", chunk_size=10, chunk_overlap=2), ["hellohello"])

    def test_chunking_with_overlap(self):
        # Length of text is 15. Chunk size 10, overlap 5.
        # Step size = 10 - 5 = 5.
        # First chunk: text[0:10] -> "0123456789"
        # Second chunk: text[5:15] -> "56789abcde"
        text = "0123456789abcde"
        expected = ["0123456789", "56789abcde"]
        self.assertEqual(chunk_text(text, chunk_size=10, chunk_overlap=5), expected)

    def test_chunking_with_no_overlap(self):
        # Length of text is 15. Chunk size 10, overlap 0.
        # Step size = 10 - 0 = 10.
        # First chunk: text[0:10] -> "0123456789"
        # Second chunk: text[10:15] -> "abcde"
        text = "0123456789abcde"
        expected = ["0123456789", "abcde"]
        self.assertEqual(chunk_text(text, chunk_size=10, chunk_overlap=0), expected)

    def test_invalid_overlap_negative(self):
        with self.assertRaises(ValueError):
            chunk_text("hello", chunk_size=10, chunk_overlap=-1)

    def test_invalid_overlap_too_large(self):
        with self.assertRaises(ValueError):
            chunk_text("hello", chunk_size=10, chunk_overlap=10)
        with self.assertRaises(ValueError):
            chunk_text("hello", chunk_size=10, chunk_overlap=15)

if __name__ == '__main__':
    unittest.main()
