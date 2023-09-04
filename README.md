# conanquest
Conquering Conan

## Develop Workflow
1. Create JUCE package (builds and exports to local cache):
```
conan create conan/JUCE
```

2. Install dependencies (generates CMake config files):
```
conan install .
```

3. Generate project files:
```
cmake --preset conan-default
```

4. Open project file:
```
open build/release/conanquest.xcodeproj
```