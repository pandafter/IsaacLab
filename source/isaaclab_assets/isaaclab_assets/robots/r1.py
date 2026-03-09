from isaaclab.sim import UsdFileCfg, RigidBodyPropertiesCfg, ArticulationRootPropertiesCfg
from isaaclab.assets import ArticulationCfg
from isaaclab.actuators import ImplicitActuatorCfg
import isaaclab.sim as sim_utils

# Ruta a tu archivo USD del robot
R1_USD_PATH = "C:/r1_usd/r1.usd"

# Configuración general de la articulación R1
R1_CFG = ArticulationCfg(
    prim_path="{ENV_REGEX_NS}/R1",
    spawn=UsdFileCfg(
        usd_path=R1_USD_PATH,
        activate_contact_sensors=True,
        rigid_props=RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.05,
            angular_damping=0.05,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=ArticulationRootPropertiesCfg(
            enabled_self_collisions=True,
            solver_position_iteration_count=12,
            solver_velocity_iteration_count=6,
        ),
        copy_from_source=False,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.78),  # ligeramente más alto para postura natural
        joint_pos={
            # Cabeza neutra
            "head_pitch_joint": 0.0,
            "head_yaw_joint": 0.0,
            # Piernas - postura erguida y estable
            "left_hip_pitch_joint": 0.05,
            "left_hip_roll_joint": 0.0,
            "left_hip_yaw_joint": 0.0,
            "left_knee_joint": 0.1,
            "left_ankle_pitch_joint": -0.05,
            "left_ankle_roll_joint": 0.0,
            "right_hip_pitch_joint": 0.05,
            "right_hip_roll_joint": 0.0,
            "right_hip_yaw_joint": 0.0,
            "right_knee_joint": 0.1,
            "right_ankle_pitch_joint": -0.05,
            "right_ankle_roll_joint": 0.0,
            # Brazos relajados
            "left_shoulder_pitch_joint": 0.0,
            "left_shoulder_roll_joint": 0.05,
            "left_shoulder_yaw_joint": 0.0,
            "left_elbow_joint": 0,
            "left_wrist_roll_joint": 0.0,
            "right_shoulder_pitch_joint": 0.0,
            "right_shoulder_roll_joint": -0.05,
            "right_shoulder_yaw_joint": 0.0,
            "right_elbow_joint": 0,
            "right_wrist_roll_joint": 0.0,
            # Cintura/Torso
            "waist_yaw_joint": 0.0,
            "waist_roll_joint": 0.0,
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        "waist": ImplicitActuatorCfg(
            joint_names_expr=["waist_yaw_joint", "waist_roll_joint"],
            stiffness=350.0,
            damping=20.0,
            velocity_limit_sim=80.0,
        ),
        "head": ImplicitActuatorCfg(
            joint_names_expr=["head_pitch_joint", "head_yaw_joint"],
            stiffness=60.0,
            damping=10.0,
            velocity_limit_sim=50.0,
        ),
        "left_leg": ImplicitActuatorCfg(
            joint_names_expr=[
                "left_hip_pitch_joint", "left_hip_roll_joint", "left_hip_yaw_joint",
                "left_knee_joint", "left_ankle_pitch_joint", "left_ankle_roll_joint"
            ],
            stiffness={
                "left_hip_pitch_joint": 300.0,
                "left_hip_roll_joint": 250.0,
                "left_hip_yaw_joint": 250.0,
                "left_knee_joint": 350.0,
                "left_ankle_pitch_joint": 400.0,  # 100 -> 400: muy rígido para evitar que se doble
                "left_ankle_roll_joint": 400.0,   # 100 -> 400
            },
            damping={
                "left_hip_pitch_joint": 12.0,
                "left_hip_roll_joint": 12.0,
                "left_hip_yaw_joint": 12.0,
                "left_knee_joint": 15.0,
                "left_ankle_pitch_joint": 25.0,  # 10 -> 25: más damping
                "left_ankle_roll_joint": 25.0,
            },
            velocity_limit_sim=100.0,
        ),
        "right_leg": ImplicitActuatorCfg(
            joint_names_expr=[
                "right_hip_pitch_joint", "right_hip_roll_joint", "right_hip_yaw_joint",
                "right_knee_joint", "right_ankle_pitch_joint", "right_ankle_roll_joint"
            ],
            stiffness={
                "right_hip_pitch_joint": 300.0,
                "right_hip_roll_joint": 250.0,
                "right_hip_yaw_joint": 250.0,
                "right_knee_joint": 350.0,
                "right_ankle_pitch_joint": 400.0,  # 100 -> 400
                "right_ankle_roll_joint": 400.0,   # 100 -> 400
            },
            damping={
                "right_hip_pitch_joint": 12.0,
                "right_hip_roll_joint": 12.0,
                "right_hip_yaw_joint": 12.0,
                "right_knee_joint": 15.0,
                "right_ankle_pitch_joint": 25.0,  # 10 -> 25
                "right_ankle_roll_joint": 25.0,
            },
            velocity_limit_sim=100.0,
        ),
        "left_arm": ImplicitActuatorCfg(
            joint_names_expr=[
                "left_shoulder_pitch_joint", "left_shoulder_roll_joint", "left_shoulder_yaw_joint",
                "left_elbow_joint", "left_wrist_roll_joint"
            ],
            stiffness=80.0,
            damping=15.0,
            velocity_limit_sim=70.0,
        ),
        "right_arm": ImplicitActuatorCfg(
            joint_names_expr=[
                "right_shoulder_pitch_joint", "right_shoulder_roll_joint", "right_shoulder_yaw_joint",
                "right_elbow_joint", "right_wrist_roll_joint"
            ],
            stiffness=80.0,
            damping=15.0,
            velocity_limit_sim=70.0,
        ),
    },
)