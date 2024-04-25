solutions = [
  {
    "name": "src",
    "url": "https://chromium-cheri/chromium.git",
    "managed": False,
    "custom_deps": {
      "src/third_party/angle": "https://github.com/chromium-cheri/angle.git@52f9fdda744bd0b443a4f34d2ed66b3ad2507f96",
      "src/third_party/boringssl/src": "https://github.com/chromium-cheri/boringssl.git@f7825d609ae29c54b50b34066e007cf2849a971e",
      "src/third_party/dawn": "https://github.com/chromium-cheri/dawn.git@2b4ef7732b02813877fea053fedadb2942444cd8",
      "src/third_party/ffmpeg": "https://github.com/chromium-cheri/ffmpeg.git@16c2dd84607867e3dcb2d8a7c4dd6f98905b9b55",
      "src/third_party/libphonenumber/dist": "https://github.com/chromium-cheri/libphonenumber.git@ee22b820126f83a584753117fcfe5b03fa4afe9c",
      "src/third_party/flac": "https://github.com/chromium-cheri/flac.git@1ae3cafc0b5c31b6bc98e95e4e36c90e29e95c09",
      "src/third_party/icu": "https://github.com/chromium-cheri/icu.git@e804a53890e579e0b3f207aebc0996a7223aa383",
      "src/third_party/libsync/src": "https://github.com/chromium-cheri/libsync.git@0b6b383c938a397112e4e876a1bd159e61dd80d1",
      "src/third_party/ruy/src": "https://github.com/chromium-cheri/ruy.git@d58ec6ed57bc4b2ab2e5c268213c0a10f75c9b74",
      "src/third_party/skia": "https://github.com/chromium-cheri/skia.git@e0eba2ca9a3673fb9f77438c0adfc8d8e5f12fda",
      "src/third_party/perfetto": "https://github.com/chromium-cheri/perfetto.git@a9cd54c32b454aac4110809b2a3347a1bf1643fd",
      "src/third_party/vulkan-deps": "https://github.com/chromium-cheri/vulkan-deps.git@b27106bd612d9001e8ef17cc8fea792d6f65c5ed",
      "src/third_party/vulkan_memory_allocator": "https://github.com/chromium-cheri/VulkanMemoryAllocator.git@f175cfc64a226e40bb2a698f217aa17065f28c74",
      "src/third_party/webrtc": "https://github.com/chromium-cheri/webrtc.git@3992c1912cac9578cfdf761e8dae91a82efbfc8c",
      "src/v8": "https://github.com/CTSRD-CHERI/v8.git@0a141bf7a20217db1a3e39a996aae4184cdf2046"
    },
    "custom_vars": {
       "checkout_nacl": False
    },
  },
]
