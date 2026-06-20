// HANDS-ON 5
// MongoDB CRUD Operations and Aggregation Framework


// TASK 1: CREATE DATABASE AND COLLECTION

// Step 60: Create Database: college_nosql

use college_nosql;


// Step 61: Create Collection: feedback

db.createCollection("feedback");


// Step 62 & 63: Insert Feedback Documents

db.feedback.insertMany([
{
    student_id: 1,
    course_code: "CS101",
    semester: "2022-ODD",
    rating: 5,
    comments: "Excellent teaching and practical examples",
    tags: ["challenging", "well-structured"],
    submitted_at: new Date("2022-11-30T10:15:00Z"),
    attachments: [
        {
            filename: "feedback1.pdf",
            size_kb: 240
        }
    ]
},
{
    student_id: 2,
    course_code: "CS101",
    semester: "2022-ODD",
    rating: 4,
    comments: "Very informative sessions",
    tags: ["practical", "interactive"],
    submitted_at: new Date("2022-11-29T09:00:00Z"),
    attachments: [
        {
            filename: "feedback2.pdf",
            size_kb: 180
        }
    ]
},
{
    student_id: 3,
    course_code: "CS101",
    semester: "2022-EVEN",
    rating: 3,
    comments: "Good but needs more examples",
    tags: ["theory", "challenging"],
    submitted_at: new Date("2022-05-20T08:00:00Z"),
    attachments: [
        {
            filename: "feedback3.pdf",
            size_kb: 150
        }
    ]
},
{
    student_id: 4,
    course_code: "CS102",
    semester: "2022-ODD",
    rating: 5,
    comments: "Loved database concepts",
    tags: ["practical", "good-examples"],
    submitted_at: new Date("2022-11-10T11:00:00Z"),
    attachments: [
        {
            filename: "feedback4.pdf",
            size_kb: 300
        }
    ]
},
{
    student_id: 5,
    course_code: "CS102",
    semester: "2022-EVEN",
    rating: 2,
    comments: "Course pace was fast",
    tags: ["challenging"],
    submitted_at: new Date("2022-06-01T12:00:00Z"),
    attachments: [
        {
            filename: "feedback5.pdf",
            size_kb: 120
        }
    ]
},
{
    student_id: 6,
    course_code: "EC101",
    semester: "2022-ODD",
    rating: 4,
    comments: "Good content delivery",
    tags: ["well-structured"],
    submitted_at: new Date("2022-11-18T10:00:00Z"),
    attachments: [
        {
            filename: "feedback6.pdf",
            size_kb: 170
        }
    ]
},
{
    student_id: 7,
    course_code: "ME101",
    semester: "2022-ODD",
    rating: 1,
    comments: "Needs improvement",
    tags: ["outdated"],
    submitted_at: new Date("2022-11-15T09:00:00Z"),
    attachments: [
        {
            filename: "feedback7.pdf",
            size_kb: 95
        }
    ]
},
{
    student_id: 8,
    course_code: "CS103",
    semester: "2022-ODD",
    rating: 5,
    comments: "Excellent course structure",
    tags: ["good-examples", "practical"],
    submitted_at: new Date("2022-11-28T08:00:00Z"),
    attachments: [
        {
            filename: "feedback8.pdf",
            size_kb: 220
        }
    ]
},
{
    student_id: 9,
    course_code: "CS103",
    semester: "2021-EVEN",
    rating: 2,
    comments: "Need better explanations",
    tags: ["challenging"],
    submitted_at: new Date("2021-12-01T10:00:00Z"),
    attachments: [
        {
            filename: "feedback9.pdf",
            size_kb: 130
        }
    ]
},
{
    student_id: 10,
    course_code: "EC101",
    semester: "2023-ODD",
    rating: 4,
    comments: "Helpful faculty support",
    tags: ["supportive", "interactive"],
    submitted_at: new Date("2023-11-30T09:00:00Z"),
    attachments: [
        {
            filename: "feedback10.pdf",
            size_kb: 210
        }
    ]
}
]);


// Step 63: Insert one document without attachments field

db.feedback.insertOne({
    student_id: 11,
    course_code: "ME102",
    semester: "2023-EVEN",
    rating: 3,
    comments: "Course content was satisfactory",
    tags: ["theory", "moderate"],
    submitted_at: new Date("2023-05-15T10:30:00Z")
});


// Step 64: Verify document count

db.feedback.countDocuments();



// TASK 2: CRUD OPERATIONS

// Step 65: Find all feedback with rating 5

db.feedback.find({
    rating: 5
});


// Step 66: Find CS101 feedback containing tag 'challenging'

db.feedback.find({
    course_code: "CS101",
    tags: "challenging"
});


// Step 67: Projection query

db.feedback.find(
    {},
    {
        _id: 0,
        student_id: 1,
        course_code: 1,
        rating: 1
    }
);


// Step 68: Add needs_review field for ratings below 3

db.feedback.updateMany(
    {
        rating: { $lt: 3 }
    },
    {
        $set: {
            needs_review: true
        }
    }
);


// Step 69: Add reviewed tag

db.feedback.updateMany(
    {
        needs_review: true
    },
    {
        $push: {
            tags: "reviewed"
        }
    }
);


// Step 70: Delete feedback from semester 2021-EVEN

db.feedback.deleteMany({
    semester: "2021-EVEN"
});


// Verify deletion

db.feedback.find({
    semester: "2021-EVEN"
});



// TASK 3: AGGREGATION PIPELINES

// Step 71: Average rating and feedback count per course

db.feedback.aggregate([
{
    $group: {
        _id: "$course_code",
        average_rating: {
            $avg: "$rating"
        },
        feedback_count: {
            $sum: 1
        }
    }
}
]);


// Step 72: Courses with average rating greater than 3

db.feedback.aggregate([
{
    $group: {
        _id: "$course_code",
        average_rating: {
            $avg: "$rating"
        },
        feedback_count: {
            $sum: 1
        }
    }
},
{
    $match: {
        average_rating: {
            $gt: 3
        }
    }
}
]);


// Step 73: Count feedback by semester

db.feedback.aggregate([
{
    $group: {
        _id: "$semester",
        total_feedback: {
            $sum: 1
        }
    }
},
{
    $sort: {
        total_feedback: -1
    }
}
]);


// Step 74: Unwind tags array

db.feedback.aggregate([
{
    $unwind: "$tags"
}
]);