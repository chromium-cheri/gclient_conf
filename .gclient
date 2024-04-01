solutions = [
  {
    "name": "src",
    "url": "https://chromium-cheri/chromium.git",
    "managed": False,
    "custom_deps": {
      "src/third_party/angle": "https://github.com/chromium-cheri/angle.git@952f9e35301eb4c2d6200b20cf245598312edd8b",
      "src/third_party/boringssl/src": "https://github.com/chromium-cheri/boringssl.git@f7825d609ae29c54b50b34066e007cf2849a971e",
      "src/third_party/libphonenumber/dist": "https://github.com/chromium-cheri/libphonenumber.git@ee22b820126f83a584753117fcfe5b03fa4afe9c",
      "src/third_party/flac": "https://github.com/chromium-cheri/flac.git@1ae3cafc0b5c31b6bc98e95e4e36c90e29e95c09",
      "src/third_party/icu": "https://github.com/chromium-cheri/icu.git@e804a53890e579e0b3f207aebc0996a7223aa383",
      "src/third_party/ruy/src": "https://github.com/chromium-cheri/ruy.git@5ab79df243d9267257279a7f38ae0d77a3f82fd7",
      "src/third_party/skia": "https://github.com/chromium-cheri/skia.git@e0eba2ca9a3673fb9f77438c0adfc8d8e5f12fda",
      "src/third_party/perfetto": "https://github.com/chromium-cheri/perfetto.git@a9cd54c32b454aac4110809b2a3347a1bf1643fd",
      "src/third_party/vulkan-deps": "https://github.com/chromium-cheri/vulkan-deps.git@b27106bd612d9001e8ef17cc8fea792d6f65c5ed",
      "src/third_party/vulkan_memory_allocator": "https://github.com/chromium-cheri/VulkanMemoryAllocator.git@19cdb6e0b7f095c545514e92fdf4e6974185497f",
      "src/third_party/webrtc": "https://github.com/chromium-cheri/webrtc.git@3992c1912cac9578cfdf761e8dae91a82efbfc8c"
    },
    "custom_vars": {
       "checkout_nacl": False
    },
  },
]
