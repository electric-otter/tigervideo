#include <iostream>
#include <vector>
#include <cmath>

struct Vertex {
    double x, y, z;
};

struct Triangle {
    Vertex v1, v2, v3;
};

struct Pixel {
    int x, y;
    int color;
    double depth;
};

// Example transformation (scaling)
Vertex transformVertex(const Vertex& vertex, double scale) {
    return {vertex.x * scale, vertex.y * scale, vertex.z * scale};
}

// Simple rasterization (stub, to be implemented properly)
std::vector<Pixel> rasterizeTriangle(const Triangle& triangle) {
    std::vector<Pixel> pixels;
    struct Point {
    float x, y;
};

struct Triangle {
    Point v1, v2, v3;
};

void drawPixel(std::vector<std::vector<int>>& image, int x, int y, int color) {
    image[x][y] = color;
}

void drawLine(std::vector<std::vector<int>>& image, Point p1, Point p2, int color) {
    // Bresenham's line algorithm 
    int x, y, dx, dy, sx, sy, err, e2;

    x = static_cast<int>(p1.x);
    y = static_cast<int>(p1.y);
    dx = abs(static_cast<int>(p2.x) - x);
    dy = abs(static_castasha_cast<int>(p2.y) - y);
    sx = p1.x < p2.x ? 1 : -1;
    sy = p1.y < p2.y ? 1 : -1;
    err = (dx > dy ? dx : -dy) / 2;

    while (true) {
        drawPixel(image, x, y, color);
        if (x == static_cast<int>(p2.x) && y == static_cast<int>(p2.y)) break;
        e2 = err;
        if (e2 > -dx) { err -= dy; x += sx; }
        if (e2 < dy) { err += dx; y += sy; }
    }
}

void drawTriangle(std::vector<std::vector<int>>& image, Triangle t, int color) {
    drawLine(image, t.v1, t.v2, color);
    drawLine(image, t.v2, t.v3, color);
    drawLine(image, t.v3, t.v1, color);
}

int main() {
    int width = 20, height = 10;
    std::vector<std::vector<int>> image(width, std::vector<int>(height, 0));

    Triangle triangle = {{1, 1}, {10, 8}, {18, 3}};
    drawTriangle(image, triangle, 1);

    for (int y = 0; y < height; y++) {
      for (int x = 0; x < width; x++) {
        std::cout << image[x][y] << " ";
      }
      std::cout << std::endl;
    }
    
    return 0;
}
    return pixels;
}

int main() {
    // Define a simple triangle
    Triangle triangle = {{0, 1, 0}, {-1, -1, 0}, {1, -1, 0}};

    // Transform the triangle
    double scale = 2;
    Triangle transformedTriangle = {
        transformVertex(triangle.v1, scale),
        transformVertex(triangle.v2, scale),
        transformVertex(triangle.v3, scale)
    };

    // Rasterize the triangle
    std::vector<Pixel> pixels = rasterizeTriangle(transformedTriangle);

    // Output the pixels (example - printing coordinates)
    for (const auto& pixel : pixels) {
        std::cout << "Pixel at (" << pixel.x << ", " << pixel.y << ") with color " << pixel.color << std::endl;
    }
    return 0;
}
