#include <dspbb/Primitives/Signal.hpp>
#include <iostream>

int main() {
	const dspbb::Signal<float> s1 = { 1, 2, 3 };
	const dspbb::Signal<float> s2 = { 3, 2, 1 };
	const auto result = s1 + s2;
	std::cout << "DSPBB installation works." << std::endl;
	return 0;
}
