EXENAME = q1

CXX = clang++
CXXFLAGS = -std=c++0x -g -O0 -Wall -Wextra

all : $(EXENAME)

$(EXENAME): q1.cpp
	$(CXX) $(CXXFLAGS) q1.cpp -o $(EXENAME)

.PHONY: clean
clean:
	rm -f $(EXENAME)
