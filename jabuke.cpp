#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <cmath>
#include <unordered_set>

// code is taken with reference to CP4 repository
using namespace std;

int N; double x,y;
const double EPS = 1e-9;

double DEG_to_RAD(double d) { return d * M_PI / 180.0; }

double RAD_to_DEG(double r) { return r*180.0 / M_PI; }

struct point { double x, y;   // only used if more precision is needed
  point() { x = y = 0.0; }                      // default constructor
  point(double _x, double _y) : x(_x), y(_y) {}        // user-defined
  bool operator == (point other) const {
   return (fabs(x-other.x) < EPS && (fabs(y-other.y) < EPS)); } 
  bool operator <(const point &p) const {
   return x < p.x || (abs(x-p.x) < EPS && y < p.y); } };

struct vec { double x, y;  // name: `vec' is different from STL vector
  vec(double _x, double _y) : x(_x), y(_y) {} };

vec toVec(point a, point b) {       // convert 2 points to vector a->b
  return vec(b.x-a.x, b.y-a.y); }

double dist(point p1, point p2) {                // Euclidean distance
  return hypot(p1.x-p2.x, p1.y-p2.y); }               // return double

// returns the perimeter of polygon P, which is the sum of
// Euclidian distances of consecutive line segments (polygon edges)
double perimeter(const vector<point> &P) {       // by ref for efficiency
  double ans = 0.0;
  for (int i = 0; i < (int)P.size()-1; ++i)      // note: P[n-1] = P[0]
    ans += dist(P[i], P[i+1]);                   // as we duplicate P[0]
  return ans;
}

// returns the area of polygon P
double area(const vector<point> &P) {
  double ans = 0.0;
  for (int i = 0; i < (int)P.size()-1; ++i)      // Shoelace formula
    ans += (P[i].x*P[i+1].y - P[i+1].x*P[i].y);
  return fabs(ans)/2.0;                          // only do / 2.0 here
}

double dot(vec a, vec b) { return (a.x*b.x + a.y*b.y); }

double norm_sq(vec v) { return v.x*v.x + v.y*v.y; }

double angle(point a, point o, point b) {  // returns angle aob in rad
  vec oa = toVec(o, a), ob = toVec(o, b);
  return acos(dot(oa, ob) / sqrt(norm_sq(oa) * norm_sq(ob))); }

double cross(vec a, vec b) { return a.x*b.y - a.y*b.x; }

// returns the area of polygon P, which is half the cross products
// of vectors defined by edge endpoints
double area_alternative(const vector<point> &P) {
  double ans = 0.0; point O(0.0, 0.0);           // O = the Origin
  for (int i = 0; i < (int)P.size()-1; ++i)      // sum of signed areas
    ans += cross(toVec(O, P[i]), toVec(O, P[i+1]));
  return fabs(ans)/2.0;
}

// note: to accept collinear points, we have to change the `> 0'
// returns true if point r is on the left side of line pq
bool ccw(point p, point q, point r) {
  return cross(toVec(p, q), toVec(p, r)) > 0;
}

// returns true if point r is on the same line as the line pq
bool collinear(point p, point q, point r) {
  return fabs(cross(toVec(p, q), toVec(p, r))) < EPS;
}

vector<point> CH_Andrew(vector<point> &Pts) {    // overall O(n log n)
  int n = Pts.size(), k = 0;
  vector<point> H(2*n);
  sort(Pts.begin(), Pts.end());                  // sort the points by x/y
  for (int i = 0; i < n; ++i) {                  // build lower hull
    while ((k >= 2) && !ccw(H[k-2], H[k-1], Pts[i])) --k;
    H[k++] = Pts[i];
  }
  for (int i = n-2, t = k+1; i >= 0; --i) {       // build upper hull
    while ((k >= t) && !ccw(H[k-2], H[k-1], Pts[i])) --k;
    H[k++] = Pts[i];
  }
  H.resize(k);
  return H;
}

// returns 1/0/-1 if point p is inside/on (vertex/edge)/outside of
// either convex/concave polygon P
int insidePolygon(point pt, const vector<point> &P) {
  int n = (int)P.size();
  if (n <= 3) return -1;                         // avoid point or line
  bool on_polygon = false;
  for (int i = 0; i < n-1; ++i)                  // on vertex/edge?
    if (fabs(dist(P[i], pt) + dist(pt, P[i+1]) - dist(P[i], P[i+1])) < EPS)
      on_polygon = true;
  if (on_polygon) return 0;                      // pt is on polygon
  double sum = 0.0;                              // first = last point
  for (int i = 0; i < n-1; ++i) {
    if (ccw(pt, P[i], P[i+1]))
      sum += angle(P[i], pt, P[i+1]);            // left turn/ccw
    else
      sum -= angle(P[i], pt, P[i+1]);            // right turn/cw
  }
  return fabs(sum) > M_PI ? 1 : -1;              // 360d->in, 0d->out
}

int main() {
    vector<point> triangle;
    for (int i = 0; i < 3; i++) {
        scanf("%lf %lf",&x,&y);
        triangle.emplace_back(x,y);
    }
    triangle.push_back(triangle[0]); // add in starting point
    printf("%.1lf\n",area(triangle));
    int belong = 0;
    scanf("%d",&N);
    for (int i = 0; i < N; i++) {
        scanf("%lf %lf",&x,&y);
        if (insidePolygon({x,y}, triangle) != -1) belong++;
    }
    printf("%d\n",belong);
    return 0;
}