solutions = [
  {
    "name": "src",
    "url": "https://chromium-cheri/chromium.git",
    "managed": False,
    "custom_deps": {
      "src/third_party/angle": "https://github.com/chromium-cheri/angle.git@952f9e35301eb4c2d6200b20cf245598312edd8b",
      "src/third_party/boringssl/src": "https://github.com/chromium-cheri/boringssl.git@cb3593f3d1ab3d0c41ffeed29143de97b9806902",
      "src/third_party/dawn": "https://github.com/chromium-cheri/dawn.git@6e86456bbd827e6eea77acc7824cd82daf070436",
      "src/third_party/libphonenumber/dist": "https://github.com/chromium-cheri/libphonenumber.git@ee22b820126f83a584753117fcfe5b03fa4afe9c",
      "src/third_party/skia": "https://github.com/chromium-cheri/skia.git@fd19dbc7d84aa6a0219869d9c3fd767f7c142712",
      "src/third_party/perfetto": "https://github.com/chromium-cheri/perfetto.git@da89612eb50db194c49898752601a59c01a8e835",
      "src/third_party/vulkan_memory_allocator": "https://github.com/chromium-cheri/VulkanMemoryAllocator.git@19cdb6e0b7f095c545514e92fdf4e6974185497f",
      "src/third_party/webrtc": "https://github.com/chromium-cheri/webrtc.git@3992c1912cac9578cfdf761e8dae91a82efbfc8c"
    },
    "custom_vars": {
       "checkout_nacl": False
    },
  },
]
