from django.shortcuts import render
import os
import json
def course_list(request):
    json_file_path = os.path.join(os.path.dirname(__file__), 'data', 'get_all_courses_API_response.json')

    with open(json_file_path,'r') as f:  # Replace with correct path
        data = json.load(f)
    
    courses = data['courses']  # Get courses from the JSON
    filters = data['facets']   # Filters for language, level, etc.
    
    return render(request, 'courses/course_list.html', {'courses': courses, 'filters': filters})

# View to show details for a selected course
def course_detail(request, course_id):
    # Load the JSON file containing course details
    json_file_path = os.path.join(os.path.dirname(__file__), 'data', 'get_course_detail_API_response.json')
    with open(json_file_path,'r') as f:
        data = json.load(f)

    # # Extract the course ID and videos (the JSON structure doesn't have 'course')
    # course_videos = data['videos']  # This contains the videos
    # course_id = data['course_id']   # Extract the course ID

    # # Render the course detail page with course info and videos
    # return render(request, 'courses/course_detail.html', {'course_id': course_id, 'videos': course_videos})
    videos = data.get('videos', [])  # Get the videos list from the JSON data

    context = {
        'course_id': course_id,  # Pass the course_id dynamically from the URL
        'videos': videos,
    }
    
    return render(request, 'courses/course_detail.html', context)
