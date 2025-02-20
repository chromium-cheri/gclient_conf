solutions = [
  {
    "name": "src",
    "url": "https://chromium-cheri/chromium.git",
    "managed": False,
    "custom_deps": {
      "src/media/cdm/api": "https://github.com/chromium-cheri/cdm.git@06dcab5c64a4bc935128c45cfcd7f2e869ad1ae7",
      "src/third_party/angle": "https://github.com/chromium-cheri/angle.git@078787aab829542ab51cecd2d003e2d9d783496a",
      "src/third_party/boringssl/src": "https://github.com/CTSRD-CHERI/boringssl.git@16e3025bef4d75edb347db72fc220e6a621b5544",
      "src/third_party/dawn": "https://github.com/chromium-cheri/dawn.git@b11037f6a91c18d7e4d9183f7d43714b595ba625",
      "src/third_party/dav1d/libdav1d": "https://github.com/chromium-cheri/dav1d.git@aa123ecb5ff5c84d74f4b00c4dc65b9328966936",
      "src/third_party/ffmpeg": "https://github.com/chromium-cheri/ffmpeg.git@2f10398a3d5f4141945d3f74bc5633c96109830f",
      "src/third_party/flac": "https://github.com/chromium-cheri/flac.git@1ae3cafc0b5c31b6bc98e95e4e36c90e29e95c09",
      "src/third_party/gemmlowp/src": "https://github.com/chromium-cheri/gemmlowp.git@3bde6c3ba21ea7ae475129c4837cb5e4e66e01f9",
      "src/third_party/icu": "https://github.com/chromium-cheri/icu.git@e804a53890e579e0b3f207aebc0996a7223aa383",
      "src/third_party/libaom/source/libaom": "https://github.com/chromium-cheri/aom.git@ed30b89bd0325936c2aecf9f69100736bf541dd8",
      "src/third_party/libphonenumber/dist": "https://github.com/chromium-cheri/libphonenumber.git@ee22b820126f83a584753117fcfe5b03fa4afe9c",
      "src/third_party/libsync/src": "https://github.com/chromium-cheri/libsync.git@0b6b383c938a397112e4e876a1bd159e61dd80d1",
      "src/third_party/libvpx/source/libvpx": "https://github.com/chromium-cheri/libvpx.git@a15ed20bd8aa05f1af26d50a53f3267421bb7e46",
      "src/third_party/openscreen/src": "https://github.com/chromium-cheri/openscreen.git@0b4c9f6b7e2a6c9099e824af2d6ed8dd663f09b7",
      "src/third_party/pdfium": "https://github.com/chromium-cheri/pdfium.git@5aa179a2ddd8a5a77a7c1a8b5eb639820604e24f",
      "src/third_party/perfetto": "https://github.com/chromium-cheri/perfetto.git@2fee9b09eb15a4e8a565cf327ebc4921ebd3a04c",
      "src/net/third_party/quiche/src": "https://github.com/chromium-cheri/quiche.git@ef71ed0abc2ecd209cdd56c95c77b4a16b8c5ccd",
      "src/third_party/ruy/src": "https://github.com/chromium-cheri/ruy.git@f30738cde26ef40b88305c367af48fb5736cc18c",
      "src/third_party/snappy/src": "https://github.com/chromium-cheri/snappy.git@7a0f716cd00154a0541fce85d9057965f9158d5b",
      "src/third_party/skia": "https://github.com/chromium-cheri/skia.git@0662b4b056680085da30ff6b1871d65dd1e89981",
      "src/third_party/sqlite/src": "https://github.com/CTSRD-CHERI/sqlite.git@15ddb6870c352b0b226b789bd2434b31f1951994",
      "src/third_party/tflite/src": "https://github.com/chromium-cheri/tflite.git@2376157b7fde75ecf848defdb269562b32b333dd",
      "src/third_party/vulkan-deps": "https://github.com/chromium-cheri/vulkan-deps.git@58f78fd4a2a3cced7f4c576b2e088407082dc569",
      "src/third_party/vulkan_memory_allocator": "https://github.com/chromium-cheri/VulkanMemoryAllocator.git@dbcf6e21325354a9dfc13e6bbebd860543844e73",
      "src/third_party/webrtc": "https://github.com/chromium-cheri/webrtc.git@743300a34a4b9fe28a8ed0e175ac9e83a1c552e7",
      "src/v8": "https://github.com/CTSRD-CHERI/v8.git@cef6cee5a6bb9219c3949562c7fb0cea03d5d1bb"
    },
    "custom_vars": {
       "checkout_nacl": False
    },
  },
]
